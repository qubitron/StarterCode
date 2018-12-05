import os

from flask import Flask, request, render_template, jsonify
from api import app
from sqlalchemy.exc import IntegrityError
from api.task import Task

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('index.html')

@app.route("/api/v1/get_all_tasks")
def get_all_tasks():
    allTasks = Task.get_all_tasks()
    return jsonify(tasks=allTasks)

@app.route("/api/v1/add_task", methods=['POST'])
def add_task():
    incoming = request.get_json()
    task = incoming.get('task')

    try:
        Task.add_task(task)
        return jsonify({'success': True}), 200

    except IntegrityError:
        return jsonify({'success': False}), 403
