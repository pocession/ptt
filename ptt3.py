# Some practice for scraping ptt
# This python scapper allows you to get article title and its review count from ptt
# Make sure the typing of sub forum name is correct, it's case sensitive

import requests
import csv
from bs4 import BeautifulSoup

name = input("Enter which sub forum you want to scrape data from: ")
page = input("How many pages do you want: ")
page = int(page)

url = "https://www.ptt.cc/bbs/"+name+"/index.html"
response = requests.get(url, cookies={'over18': '1'})
result = response.text
soup = BeautifulSoup(result, 'html.parser')

# Check how many articles and make a list for storing all url of scrapped pages
pagelist = []

# Store the first page
a = soup.find_all('a', attrs={'class':'btn wide'})
page_number = a[1]['href']
page_scrapped = "https://www.ptt.cc/bbs/"+name+"/index.html"
pagelist.append(page_scrapped)

# Get page number
# Extract page number by replace non-integer characters with NONE
# Plus 1 page to page number for index
fix = "/bbs/{url}/index".format(url = name)
page_number = int(page_number.replace("{a}".format(a = fix),"").replace(".html","")) + 1
print("Total page number is {a}.".format(a = page_number))

# Get url of pages
k = 0
while k < page:
    page_scrapped_x = page_number - (k)
    page_scrapped_y = str(page_scrapped_x)
    page_scrapped_y = "https://www.ptt.cc/bbs/"+name+"/index"+page_scrapped_y+".html"
    pagelist.append(page_scrapped_y)
    k += 1
print("Get all url of pages ... done")

# Create a csv file
csvfile = open("{a}.csv".format(a = name),'w',newline='')
writer = csv.writer(csvfile, delimiter=',')

# Write header of csv
writer.writerow(['article_review','article_title'])
csvfile.close()
print("Write title ... done")

count = 1
i = 0
while i < len(pagelist):
    url = pagelist[i]
    print("Now get data from {a}".format(a = url))
    response = requests.get(url, cookies={'over18': '1'})
    result = response.text
    soup = BeautifulSoup(result, 'html.parser')
    article_review = soup.find_all('div',attrs={'class':'nrec'})
    article_title = soup.find_all('div', attrs={'class':'title'})

    m = 0
    n = 0

    while m < len(article_review) and n < len(article_title):
        x = article_review[m].text
        if x == '':
            x = x.replace('','0')
        if x == '爆':
            x = '99'
        x = int(x)
        y = article_title[n]
        y = y.text.replace("\n","").replace(" ","").replace("\t","")
        csvrow = [x,y]

        csvfile2 = open("{a}.csv".format(a = name),"a",newline='')
        writer = csv.writer(csvfile2, delimiter=',')
        writer.writerow(csvrow)
        m+=1
        n+=1

    print("page {a} ... done".format(a = count))
    count+=1
    i+=1
print("done")