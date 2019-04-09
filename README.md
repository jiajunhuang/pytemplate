# Python 后端开发框架模板

- Flask
- SQLAlchemy
- Marshamallow

```bash
# 可以使用MySQL，把URI改掉，并且更改 requirements.txt里的驱动即可
$ export SQLALCHEMY_DB_URI='postgresql+psycopg2://<用户>:<密码>@<地址>/<数据库>'
$ ./revision.sh init  # 生成第一个数据库migration
```

用法：

```bash
$ git clone git@github.com:jiajunhuang/pytemplate.git repo # 克隆本仓库
$ cd repo  # 进入代码
$ rm -rf .git  # 删除原本git信息
$ git init  # 重新初始化仓库
```

然后就可以开始开发了
