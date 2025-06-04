#

## 预装

- docker <https://docker.com>
- pnpm `npm i -g pnpm`
- mkcert `brew install mkcert`
- black `pip install "black[jupyter]"`

## 准备

```bash
sh scripts/install.sh

```

## 本地开发

```bash
sh scripts/dev.sh
```

## 调试

- 本地访问地址 <https://localhost:9999/>

- API 文档 <https://localhost:9999/api/docs>

## 格式化

```bash
sh scripts/lint.sh
```

## 数据库

```bash
mysql -h 127.0.0.1 -P 63406 -u myuser -p'mypassword'
```

也可以在开发环境中直接使用 phpmyadmin <https://localhost:9999/phpmyadmin/>
