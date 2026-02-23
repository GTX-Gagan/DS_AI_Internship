import sqlite3
import pandas as pd

conn = sqlite3.connect('interns.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    intern_id INTEGER PRIMARY KEY,
    intern_name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER NOT NULL
);
""")

cursor.execute("DELETE FROM interns;")

cursor.executemany("""
INSERT INTO interns (intern_id, intern_name, track, stipend)
VALUES (?, ?, ?, ?);
""", [
    (101, 'Ravi', 'Data Science', 6000),
    (102, 'Sneha', 'Web Development', 4500),
    (103, 'Arjun', 'AI/ML', 7000),
    (104, 'Priya', 'Data Science', 5500),
    (105, 'Karan', 'Web Development', 5200)
])

conn.commit()

filter_query = """
SELECT *
FROM interns
WHERE track = 'Data Science'
AND stipend > 5000;
"""

avg_query = """
SELECT 
    track,
    AVG(stipend) AS average_stipend
FROM interns
GROUP BY track;
"""

count_query = """
SELECT 
    track,
    COUNT(*) AS total_interns
FROM interns
GROUP BY track;
"""

df_filter = pd.read_sql_query(filter_query, conn)
df_avg = pd.read_sql_query(avg_query, conn)
df_count = pd.read_sql_query(count_query, conn)

print("Filtered Interns:")
print(df_filter)

print("\nAverage Stipend Per Track:")
print(df_avg)

print("\nIntern Count Per Track:")
print(df_count)

conn.close()