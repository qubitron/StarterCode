from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from api.api import app, Task
from api import db

from test.test_data import tasks


migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()

@manager.command
def create_test_data():
    # Reset the database to original state
    create_db()
    Task.query.delete()

    for task in tasks:
        Task.add_task(task)

if __name__ == '__main__':
    manager.run()
