# Demo how to read csv and write it into database

import sqlite3
import csv

conn = sqlite3.connect('ptt.db')
c = conn.cursor()
csvfile = open('Japan_Travel.csv','r')
rowreader = csv.reader(csvfile,delimiter=',')
article_list=[]
for row in rowreader:
    article_list.append(row)

i = 1
while i < 7:
    element = article_list[i]
    title = element[0]
    review = element[1]
    article_id = element[2]
    item=[title, review, article_id]
    c.execute('''INSERT INTO ARTICLE (TITLE, REVIEW, ID) VALUES(?,?,?)''',item)
    i+=1



conn.commit()
conn.close()
print("OK")