# _*_ coding:utf-8 _*_
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from application.app import create_app
from application.database import db_sqlite


app = create_app()
manager = Manager(app)

migrate = Migrate(app, db_sqlite)
manager.add_command('db', MigrateCommand)


@manager.command
def runserver():
    app.run(host=app.config['HOST'])


if __name__ == '__main__':
    manager.run(default_command='runserver')