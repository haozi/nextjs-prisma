import hashlib
import json
import os
import subprocess
import textwrap
from datetime import datetime
from zoneinfo import ZoneInfo

BASE_DIR = os.path.abspath(os.path.join(__file__, "../.."))
os.chdir(BASE_DIR)

now = datetime.now(ZoneInfo("Asia/Shanghai"))
TIMESTAMP = now.strftime("%Y-%m-%dT%H:%M:%S%z")

BACKUP_DIR = "./psy-data-backup"
JSON_FILE = os.path.join(BACKUP_DIR, "backup.json")
CONTAINER_NAME = "backup-container"
IMAGE_NAME = "ghcr.io/haozi/alpine:latest"
BACKUP_PATH = "/tmp/backup.tgz"
BACKUP_PASSWORD = os.getenv("BACKUP_PASSWORD", "default_secure_password")
END_MARKER = f"--------------------- END OF BACKUP {TIMESTAMP} ---------------------"

os.makedirs(BACKUP_DIR, exist_ok=True)

# 清理旧的容器
subprocess.run(
    ["docker", "rm", "-f", CONTAINER_NAME],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)

# 运行备份容器
print("Starting backup process...")
subprocess.run(
    textwrap.dedent(
        f"""\
    docker run -d --name {CONTAINER_NAME} \\
        --privileged --pid=host \\
        {IMAGE_NAME} \\
        nsenter -t 1 -m -u -n -i sh -c \\
        "cd /var/lib/docker && tar czvf {BACKUP_PATH} ./volumes/ && echo '{END_MARKER}' && sleep infinity"
"""
    ),
    shell=True,
    check=True,
)

# 监听日志，等待备份完成
print("Waiting for backup to complete...")
log_process = subprocess.Popen(
    ["docker", "logs", "-f", CONTAINER_NAME],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

while True:
    line = log_process.stdout.readline()
    if not line:
        continue
    print(line.strip())
    if END_MARKER in line:
        print("Backup completed!")
        break

log_process.terminate()

# 读取备份文件
backup_file_path = os.path.join(BACKUP_DIR, "backup.tgz")
with open(backup_file_path, "wb") as f:
    subprocess.run(
        ["docker", "exec", CONTAINER_NAME, "cat", BACKUP_PATH], stdout=f, check=True
    )


# 计算 MD5
def calculate_md5(file_path):
    md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
    return md5.hexdigest()


md5_hash = calculate_md5(backup_file_path)
final_backup_path = os.path.join(BACKUP_DIR, f"{md5_hash}.tgz")
os.rename(backup_file_path, final_backup_path)

# **🔐 使用 7z 加密备份**
ENCRYPTED_BACKUP_PATH = final_backup_path + ".7z"


subprocess.run(
    [
        "7z",
        "a",
        ENCRYPTED_BACKUP_PATH,
        final_backup_path,
        "-mx=9",  # 最高压缩级别
        f"-p{BACKUP_PASSWORD}",  # 设置密码
        "-mhe=on",  # 开启文件名加密
    ],
    check=True,
)

print(f"Encrypted backup saved: {ENCRYPTED_BACKUP_PATH}")

# **🗑️ 删除未加密的 `.tgz` 文件**
os.remove(final_backup_path)
print(f"Deleted unencrypted backup: {final_backup_path}")

# 记录备份信息
backup_data = {}
if os.path.exists(JSON_FILE):
    with open(JSON_FILE, "r") as f:
        backup_data = json.load(f)

backup_data[TIMESTAMP] = md5_hash
backup_data = dict(sorted(backup_data.items(), key=lambda x: x[0], reverse=True))

with open(JSON_FILE, "w") as f:
    json.dump(backup_data, f, indent=2)
    f.write("\n")

# 删除容器
subprocess.run(
    ["docker", "rm", "-f", CONTAINER_NAME],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)

print(f"Backup process complete. Only encrypted file remains: {ENCRYPTED_BACKUP_PATH}")
print(f"Updated {JSON_FILE}")


"""debug"""
# docker run -it \
#     --privileged --pid=host \
#     ghcr.io/haozi/alpine:latest \
#     nsenter -t 1 -m -u -n -i sh
