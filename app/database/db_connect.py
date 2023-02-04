import sqlite3


conn = sqlite3.connect('app/database/todolist.db')

# Create a cursor
cursor = conn.cursor()

# Execute a CREATE TABLE  for tasks table
cursor.execute('''
    CREATE TABLE tasks(
        id INTEGER PRIMARY KEY,
        task_list_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        is_completed INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY(task_list_id) REFERENCES task_lists(id)
    );
''')

# Execute a CREATE TABLE  for task_lists table
cursor.execute('''
    CREATE TABLE task_lists(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );
''')


# Commit the transaction
conn.commit()

# Close the connection
conn.close()
