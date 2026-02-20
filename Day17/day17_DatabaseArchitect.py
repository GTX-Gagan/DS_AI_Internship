import sqlite3
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")
cursor.execute("INSERT INTO interns VALUES (1, 'Gagan', 'Data Science', 15000)")
cursor.execute("INSERT INTO interns VALUES (2, 'Pranav', 'Web Dev', 12000)")
cursor.execute("INSERT INTO interns VALUES (3, 'Pradeep', 'Data Science', 18000)")
cursor.execute("INSERT INTO interns VALUES (4, 'Hanith', 'UI/UX', 14000)")
cursor.execute("INSERT INTO interns VALUES (5, 'Sathwik', 'Web Dev', 13000)")
conn.commit()
cursor.execute("SELECT name, track FROM interns")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()