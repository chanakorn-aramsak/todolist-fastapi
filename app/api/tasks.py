from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.get("/tasks/")
def get_tasks():
    # Connect to the database
    conn = sqlite3.connect("app/database/todolist.db")
    cursor = conn.cursor()

    # Retrieve all tasks from the database
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    # Close the connection
    conn.close()

    return {"tasks": tasks}




@app.post("/tasks/")
def add_task(task_list_id: int, description: str):
    # Connect to the database
    conn = sqlite3.connect("app/database/todolist.db")
    cursor = conn.cursor()

    # Insert the new task into the database
    cursor.execute("INSERT INTO tasks (task_list_id, description) VALUES (?, ?)",
                   (task_list_id, description))
    conn.commit()

    # Retrieve the newly added task
    cursor.execute(
        "SELECT * FROM tasks WHERE id = (SELECT MAX(id) FROM tasks)")
    task = cursor.fetchone()

    # Close the connection
    conn.close()

    return {"task": task}
