from api import db


class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    task = db.Column(db.String(255))

    def __init__(self, task):
        self.task = task
    
    @staticmethod
    def add_task(task):
        taskToAdd = Task(task)

        db.session.add(taskToAdd)
        db.session.commit()
    
    @staticmethod
    def get_all_tasks():
        return [t.task for t in Task.query.all()]
