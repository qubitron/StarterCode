from ..api import db
from ..api.task import Task

tasks = [
    "Download the recommended extensions (i.e. App Service)",
    "Use a free guest account to access Azure",
    "Create a free App Service instance",
    "Create a free Azure Database for Postgres instance and connect it to your App Service instance",
    "Deploy this application to the App Service instance",
    "View your new website in the browser!"
]

session = db.session()

if __name__ == '__main__':
    db.create_all()

    for task in tasks:
        Task.add_task(task)
