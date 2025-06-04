- 本地数据库连接

在当前文件夹下创建 .env 文件，添加以下内容

```
DATABASE_URL="postgresql://myuser:mypassword@localhost:65432/psy-test-db"
```

- 初始化数据库

```
pnpm prisma migrate dev
```
