{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter which sub forum you want to scrape data from: Japan_Travel\n",
      "How many pages do you want: 10\n"
     ]
    }
   ],
   "source": [
    "# Some practice for scraping ptt\n",
    "# More functions\n",
    "\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "name = input(\"Enter which sub forum you want to scrape data from: \")\n",
    "page = input(\"How many pages do you want: \")\n",
    "page = int(page)\n",
    "\n",
    "url = \"https://www.ptt.cc/bbs/\"+name+\"/index.html\"\n",
    "response = requests.get(url, cookies={'over18': '1'}) \n",
    "result = response.text\n",
    "soup = BeautifulSoup(result, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6505\n",
      "['https://www.ptt.cc/bbs/Japan_Travel/index.html', 'https://www.ptt.cc/bbs/Japan_Travel/index6505.html', 'https://www.ptt.cc/bbs/Japan_Travel/index6504.html', 'https://www.ptt.cc/bbs/Japan_Travel/index6503.html', 'https://www.ptt.cc/bbs/Japan_Travel/index6502.html', 'https://www.ptt.cc/bbs/Japan_Travel/index6501.html', 'https://www.ptt.cc/bbs/Japan_Travel/index6500.html', 'https://www.ptt.cc/bbs/Japan_Travel/index6499.html', 'https://www.ptt.cc/bbs/Japan_Travel/index6498.html', 'https://www.ptt.cc/bbs/Japan_Travel/index6497.html', 'https://www.ptt.cc/bbs/Japan_Travel/index6496.html']\n"
     ]
    }
   ],
   "source": [
    "# Check how many articles and make a list for storing all url of scrapped pages\n",
    "pagelist = []\n",
    "\n",
    "# Store the first page\n",
    "a = soup.find_all('a', attrs={'class':'btn wide'})\n",
    "page_number = a[1]['href']\n",
    "page_scrapped = \"https://www.ptt.cc/bbs/\"+name+\"/index.html\"\n",
    "pagelist.append(page_scrapped)\n",
    "\n",
    "# Get article number\n",
    "fix = \"/bbs/{url}/index\".format(url = name)\n",
    "page_number = int(page_number.replace(\"{x}\".format(x = fix),\"\").replace(\".html\",\"\"))\n",
    "print(page_number)\n",
    "\n",
    "k = 0\n",
    "while k < page:\n",
    "    page_scrapped_x = page_number - (k)\n",
    "    page_scrapped_y = str(page_scrapped_x)\n",
    "    page_scrapped_y = \"https://www.ptt.cc/bbs/\"+name+\"/index\"+page_scrapped_y+\".html\"\n",
    "    pagelist.append(page_scrapped_y)\n",
    "    k += 1\n",
    "print(pagelist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total review counts:  10\n",
      "Total article number: 10\n",
      "1 [讓售]JR西日本關西廣域鐵路5日券實體票4張分售\n",
      "0 [遊記]富士山一日遊\n",
      "0 [問題]麵包超人列車\n",
      "0 [讓售]東京地鐵24小時卷\n",
      "0 [食記]金澤町家鬆餅咖啡Cafeたもん\n",
      "1 [問題]關西9天8夜行程請益(滋賀)\n",
      "0 (本文已被刪除)[hugossa]\n",
      "0 [食記]上野沼津港海將午餐海鮮丼吃到飽\n",
      "48 [公告]日本旅遊板板規107.06\n",
      "99 [公告]108.2實況回報(含天氣/物候/穿著詢問)\n"
     ]
    }
   ],
   "source": [
    "# Get review counts + title\n",
    "article_review = soup.find_all('div',attrs={'class':'nrec'})\n",
    "article_title = soup.find_all('div', attrs={'class':'title'})\n",
    "print(\"Total review counts: \",len(article_review))\n",
    "print(\"Total article number:\",len(article_title))\n",
    "i = 0\n",
    "j = 0\n",
    "while i < len(article_review) and j < len(article_title):\n",
    "    x = article_review[i].text\n",
    "    if x == '':\n",
    "        x = x.replace('','0')\n",
    "    if x == '爆':\n",
    "        x = '99'\n",
    "    x = int(x)\n",
    "    y = article_title[j]\n",
    "    print(x,y.text.replace(\"\\n\",\"\").replace(\" \",\"\").replace(\"\\t\",\"\"))\n",
    "    i+=1\n",
    "    j+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total review counts:  20\n",
      "Total article number: 20\n",
      "2 Re:[問題]北海道札幌雪祭+道東行程順序?\n",
      "2 [問題]請問日本的藥妝店可以使用suica嗎？\n",
      "3 [徵人]2/28柯南密室逃脫(USJ)\n",
      "1 [讓售]大阪地鐵一日券x3\n",
      "17 [問題]Klook買JRPASS的問題\n",
      "5 [資訊]20190225匯率\n",
      "0 [食記]福岡博多站週邊午間御膳博多華味鳥3訪\n",
      "0 [遊記]九州賞楓雜記1\n",
      "3 [問題]3/4~3/10東京行程請益\n",
      "4 [問題]東京迪士尼假期套票\n",
      "3 [問題]河內藤園超商購票一問\n",
      "0 [食記]東京敘庵最後一個方案1980円燒肉吃到飽\n",
      "0 [讓售]京阪神阪急全線自由乘車券一日券\n",
      "0 (本文已被刪除)[blankptt]\n",
      "0 [讓售]3/20MLB海外開幕戰水手V.S運動家三壘\n",
      "18 [問題]JR仙山線山形到仙台通勤時間的狀況\n",
      "5 [問題]櫻花季的保津川遊船值得去嗎？需要預約？\n",
      "3 [遊記]2/23神奈川西平畑公園賞河津櫻\n",
      "1 [徵人][共乘]3/1或3/2藏王狐狸村(去回)\n",
      "3 [徵人]3/2東京巨蛋看棒球　免費(洽談中)\n"
     ]
    }
   ],
   "source": [
    "# Get next pages\n",
    "\n",
    "url = pagelist[1]\n",
    "response = requests.get(url, cookies={'over18': '1'}) \n",
    "result = response.text\n",
    "soup = BeautifulSoup(result, 'html.parser')\n",
    "\n",
    "article_review = soup.find_all('div',attrs={'class':'nrec'})\n",
    "article_title = soup.find_all('div', attrs={'class':'title'})\n",
    "print(\"Total review counts: \",len(article_review))\n",
    "print(\"Total article number:\",len(article_title))\n",
    "i = 0\n",
    "j = 0\n",
    "while i < len(article_review) and j < len(article_title):\n",
    "    x = article_review[i].text\n",
    "    if x == '':\n",
    "        x = x.replace('','0')\n",
    "    if x == '爆':\n",
    "        x = '99'\n",
    "    x = int(x)\n",
    "    y = article_title[j]\n",
    "    print(x,y.text.replace(\"\\n\",\"\").replace(\" \",\"\").replace(\"\\t\",\"\"))\n",
    "    i+=1\n",
    "    j+=1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your address: https://www.ptt.cc/bbs/Beauty/M.1551006817.A.E04.html\n",
      "['https://i.imgur.com/E1Pauwi.jpg', 'https://i.imgur.com/Gj8TCQn.jpg', 'https://i.imgur.com/RU7gfXr.jpg', 'https://i.imgur.com/3xJEZg1.jpg']\n"
     ]
    }
   ],
   "source": [
    "# Get all pictures from a specific post\n",
    "\n",
    "import requests\n",
    "import re\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "url = input(\"Enter your address: \")\n",
    "response = requests.get(url, cookies={'over18': '1'}) \n",
    "result = response.text\n",
    "soup = BeautifulSoup(result, 'html.parser')\n",
    "soup = soup.find_all('meta', attrs={'property':''})\n",
    "soup = soup[4]\n",
    "soup = str(soup)\n",
    "soup\n",
    "\n",
    "image_url = re.findall(\"https://[a-z].imgur.com/[0-9a-zA-Z]{7}.[a-zA-z]{3}\",soup)\n",
    "\n",
    "k = 0\n",
    "\n",
    "while k < len(image_url):\n",
    "    filename = image_url[k].split(\"/\")[-1]\n",
    "    r = requests.get(image_url[k], timeout=0.5, stream=True)\n",
    "    if r.status_code == 200:\n",
    "        f = open(filename,'wb')\n",
    "        f.write(r.content)\n",
    "    k += 1\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get url of all images and store images with the name = url\n",
    "\n",
    "filename = url.split(\"/\")[-1]\n",
    "print(filename)\n",
    "r = requests.get(url, timeout=0.5, stream=True)\n",
    "print(r)\n",
    "\n",
    "if r.status_code == 200:\n",
    "    with open(filename,'wb') as f:\n",
    "        f.write(r.content)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
