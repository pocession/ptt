import sqlite3

conn = sqlite3.connect('ptt.db')
c = conn.cursor()

cursor = c.execute("SELECT id FROM article_large")
temp1=[]
for row in cursor:
    temp1.append(row)
print("old table is:",len(temp1))

cursor2 = c.execute("DELETE FROM article_large WHERE ROWID NOT IN (SELECT MIN(ROWID) from article_large GROUP BY id)")
conn.commit()

cursor3 = c.execute("SELECT id FROM article_large")
temp3=[]
for row in cursor3:
    temp3.append(row)
print("new table is:",len(temp3))