# _*_ coding:utf-8 _*_
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import app
from model import db as db_sqlite

manager = Manager(app)
migrate = Migrate(app, db_sqlite)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()