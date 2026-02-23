import sqlite3
import pandas as pd
conn = sqlite3.connect('interns.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    intern_id INTEGER PRIMARY KEY,
    intern_name TEXT NOT NULL,
    track TEXT NOT NULL
);""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT NOT NULL,
    track TEXT NOT NULL);""")
cursor.execute("DELETE FROM interns;")
cursor.executemany("""
INSERT INTO interns (intern_id, intern_name, track)
VALUES (?, ?, ?);
""", [
    (101, 'Ravi', 'Data Science'),
    (102, 'Sneha', 'Web Development'),
    (103, 'Arjun', 'AI/ML')])
cursor.execute("DELETE FROM mentors;")
cursor.executemany("""
INSERT INTO mentors (mentor_id, mentor_name, track)
VALUES (?, ?, ?);
""", [
    (1, 'Alice Johnson', 'Data Science'),
    (2, 'Rahul Sharma', 'Web Development'),
    (3, 'Meera Iyer', 'AI/ML')])
conn.commit()
query = """
SELECT 
    interns.intern_name,
    interns.track,
    mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""
df = pd.read_sql_query(query, conn)
print(df)
conn.close()