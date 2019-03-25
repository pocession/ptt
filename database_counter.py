import sqlite3

conn = sqlite3.connect('ptt.db')
c = conn.cursor()
cursor = c.execute("SELECT id from article_large WHERE content IS NULL ")
conn.commit()
articleid_list=[]
for row in cursor:
    articleid_list.append(row)
cursor.close()
print("Total number of article without any contents:",len(articleid_list))