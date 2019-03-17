# Demo how to read csv and write it into database
# Select 遊記 from csv file AND write into database

import sqlite3
import csv

conn = sqlite3.connect('ptt.db')
c = conn.cursor()
csvfile = open('Japan_Travel_clean.csv','r')
rowreader = csv.reader(csvfile,delimiter=',')
article_list=[]
for row in rowreader:
    article_list.append(row)
print("Total article number: ",len(article_list) - 1)

i = 1
new_list=[]
while i < len(article_list):
    element = article_list[i]
    if element[0].find('[遊記]') == 0 and element[0].find('沖繩') != -1:
        new_list.append(element)
    i+=1
print("Total 遊記 about 沖繩 numer is: ",len(new_list))

j = 0
while j < len(new_list):
    element = new_list[j]
    title = element[0]
    review = element[1]
    article_id = element[2]
    item=[title, review, article_id]
    c.execute('''INSERT INTO article (title, review, id) VALUES(?,?,?)''',item)
    j+=1


conn.commit()
conn.close()
print("OK")