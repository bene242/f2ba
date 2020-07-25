import sqlite3

conn = sqlite3.connect('employees.db')
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        years INTEGER DEFAULT 0
    )
""")

cur.executemany("""
    INSERT INTO employees (first_name, last_name, email, years) VALUES (?,?,?,?)
""", [
    ('Kevin','Bacon', 'kbacon@exa.com',2),
    ('Josh','Brolin', 'jbrolin@exa.com',1),
    ('Kim','Dickens', 'kdickens@exa.com',0)
])

conn.commit()

cur.execute("select * from employees")
print(cur.fetchall())

cur.close()
conn.close()
