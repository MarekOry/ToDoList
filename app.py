import psycopg2
from datetime import datetime, timezone
from flask import Flask, request
#Project files:
import db_connector
import repository

app = Flask(__name__)

connection = db_connector.connection

@app.post('/api/post/todo')
def post_todo():
    data = request.get_json()
    todo = data["todo"]
    try:
        creation_date = datetime.strptime(data["creation_date"], "%Y-%m-%d")
    except KeyError:
        creation_date = datetime.now(timezone.utc)
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(repository.INSERT_LIST, (todo, creation_date))
            id = cursor.fetchone()[0]
    return {"id": id, "message": f'todo {todo} created on {creation_date}.'}


@app.get('/api/get/todo')
def get_todo():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(repository.SELECT_LIST)
            rows = cursor.fetchall()
            for row in rows:
                return rows


@app.put('/api/put/todo')
def put_todo():
    data = request.get_json()
    id = data["id"]
    todo = data["todo"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(repository.PUT_LIST, (todo, id))
    return {"id": id, "message": f'todo value has been changed to {todo}'}


@app.delete('/api/delete/todo')
def delete_todo():
    data = request.get_json()
    id = data["id"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(repository.DELETE_LIST, (id,))
    return {"id": id, "message": f'todo has been removed.'}
