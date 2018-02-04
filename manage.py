# Author: c.evan
# -*- coding: utf-8 -*-


from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from ihome import create_app

# 应该由manage文件来创建app, 通过传入参数来实现调试和发布的切换
app, db = create_app('develop')

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
