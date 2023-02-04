from fastapi import APIRouter, HTTPException
import sqlite3

router = APIRouter()

  
@router.get("/")
def get_first_pages():
    return "hello there this is first page"

def get_db_connection():
    conn = sqlite3.connect("app/database/todolist.db")
    cursor = conn.cursor()
    return conn, cursor
  
@router.get("/tasks/")
def get_tasks():
    conn, cursor = get_db_connection()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    return {"tasks": tasks}


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    conn, cursor = get_db_connection()

    cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = cursor.fetchone()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    conn.close()
    return {"task": task}


@router.post("/tasks/")
def add_task(description: str, date: str):
    conn, cursor = get_db_connection()

    cursor.execute("INSERT INTO tasks (description, date) VALUES (?, ?)",
                   (description, date))
    conn.commit()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = (SELECT MAX(id) FROM tasks)")
    task = cursor.fetchone()

    conn.close()
    return {"task": task}


@router.put("/tasks/{task_id}")
def update_task(task_id: int, description: str, date: str):
    conn, cursor = get_db_connection()

    cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = cursor.fetchone()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    cursor.execute("UPDATE tasks SET description=?, date=? WHERE id=?",
                   (description, date, task_id))
    conn.commit()

    cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = cursor.fetchone()

    conn.close()
    return {"task": task}


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn, cursor = get_db_connection()

    cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = cursor.fetchone()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

    conn.close()
    return {"task_id": task_id}
