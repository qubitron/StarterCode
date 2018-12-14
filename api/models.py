from api import db


class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(255))

    def __init__(self, description):
        self.description = description
    
    @staticmethod
    def create_task_from_json(task):
        taskToAdd = Task(task)

        db.session.add(taskToAdd)
        db.session.commit()
    
    @staticmethod
    def get_all_tasks():
        return [t.description for t in Task.query.all()]
