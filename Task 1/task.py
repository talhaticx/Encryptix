import sqlite3
    
class Database():
    def __init__(self, name):
        self.conn = sqlite3.connect(f"./databases/{name}.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL UNIQUE,
                description TEXT
                completed INTEGER DEFAULT 0
            )
        ''')
    
    def add_task(self, task):
        try:
            self.cursor.execute('''
                INSERT INTO tasks (title, description)
                VALUES (?, ?)
            ''', (task.title, task.description))
        except sqlite3.IntegrityError:
            print("Task with the same title already exists.")
        self.conn.commit()
    
    def remove_task(self, identifier):
        self.cursor.execute('''
            DELETE FROM tasks
            WHERE id = ?
        ''', (identifier,))
        self.conn.commit()

        
    def update_description(self, identifier, description=None):
        self.cursor.execute('''
            UPDATE tasks
            SET description = ?
            WHERE id = ?
        ''', (description, identifier))
        self.conn.commit()
    
    def update_completed(self, identifier):
        self.cursor.execute('''
            UPDATE tasks
            SET completed = 1
            WHERE id = ?
        ''', (identifier))
        self.conn.commit()
    
    def query(self):
        self.cursor.execute("SELECT * FROM tasks")
        rows = self.cursor.fetchall()
        return rows
    
    def exit(self):
        self.cursor.close()
        self.conn.close()