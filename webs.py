import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import MeCab

#r = requests.get('https://news.yahoo.co.jp')
#
#print(r.headers)
#print("--------")
#print(r.encoding)
#print(r.content)

html = "<h1>sayhello</h1>,<h1>saysay</h1>,<h2>say</h2>"
 
soup = BeautifulSoup(html, "html.parser")
 
print(soup.select("h1"))

#----------------------------------------------------------------------
#r = requests.get("https://news.yahoo.co.jp/")
r = requests.get("https://news.yahoo.co.jp/topics/top-picks")

soup = BeautifulSoup(r.content, "html.parser")
 
print(soup.title)

# ニュース一覧を抽出
#print(soup.find("ul", "newsFeed_list").text)

#----------------------------------------------------------------------
#mecab = MeCab.Tagger()
#text = mecab.parse( soup.find("ul", "newsFeed_list").text )
#print(text)
tags = soup.find_all("div", "newsFeed_item_title")
#text = soup.find("ul", "newsFeed_list").text

text = ""

for tag in tags:
    #print(tag.string)
    text = text + " " + tag.string

wakati = MeCab.Tagger("-Owakati")
#print(wakati.parse( text ))
words = wakati.parse( text )

wc = WordCloud(font_path='C:/Windows/Fonts/yumin.ttf', width=1024, height=768, background_color="white")
wc.generate(words)
wc.to_file('wc2.png')

print(text)