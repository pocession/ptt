# Demo how to read csv and write it into database
# Select articles with id from csv file AND write into database

import sqlite3
import csv

conn = sqlite3.connect('ptt.db')
c = conn.cursor()
csvfile = open('Japan_Travel_clean.csv','r')
rowreader = csv.reader(csvfile,delimiter=',')
article_list=[]
for row in rowreader:
    article_list.append(row)
print("Total article number is: ",len(article_list) - 1)

i = 1
new_list=[]
while i < len(article_list):
    element = article_list[i]
    new_list.append(element)
    i+=1

j = 0
k = 0
while j < len(new_list):
    element = new_list[j]
    title = element[0]
    review = element[1]
    article_id = element[2]
    item=[title, review, article_id]
    if article_id != '':
        c.execute('''INSERT INTO article_large (title, review, id) VALUES(?,?,?)''',item)
        k+=1
    j+=1
print("The actual article number written in the database is: ",k)

conn.commit()
conn.close()
print("OK")