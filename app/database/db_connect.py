import sqlite3


conn = sqlite3.connect('app/database/todolist.db')

# Create a cursor
cursor = conn.cursor()

# Execute a CREATE TABLE  for tasks table
cursor.execute('''
    CREATE TABLE tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        task_description TEXT NOT NULL,
        status INTEGER NOT NULL
    );
''')

# Execute a CREATE TABLE  for task_lists table
cursor.execute('''
    CREATE TABLE task_lists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        list_name TEXT NOT NULL,
        list_description TEXT NOT NULL
    );
''')

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
