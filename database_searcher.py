import sqlite3
article_number = int(input("How many articles you want to search for? "))
inputlist=[]
i = 0
while i < article_number:
    inputlist.append(input("Enter your {a}th article: ".format(a=i)))
    i+=1
conn = sqlite3.connect('ptt.db')
c = conn.cursor()
for element in inputlist:
    cursor = c.execute("SELECT * from article_large WHERE id = ?",(element,))
    for item in cursor:
        print(item)
cursor.close()