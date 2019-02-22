import os

from flask import Flask, jsonify, render_template, request
from sqlalchemy.exc import IntegrityError

from api import app
from api.models import Task


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/api/v1/get_all_tasks", methods=['GET'])
def get_all_tasks():
    allTasks = Task.get_all_tasks()
    return jsonify(tasks=allTasks)

@app.route("/api/v1/add_task", methods=['POST'])
def add_task():
    incoming = request.get_json()
    task = incoming.get('task')

    try:
        Task.create_task_from_json(task)
        resp = jsonify({'success': True}), 200
       
    except IntegrityError:
        resp = jsonify({'success': False}), 403
    
    return resp
