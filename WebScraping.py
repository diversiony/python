import requests
import pandas as pd
from bs4 import BeautifulSoup

#print (requests.get("https://dividable.net").text)

category_li_path = "nav#category ul li a"
res = requests.get("https://dividable.net").text
soup = BeautifulSoup(res, 'html.parser')
lines = soup.select(category_li_path)
category_dict = {}
for line in lines:
    category_dict[line.get("href")] = line.string
    print(line.get("href") + " " + line.string)

category_res = requests.get("https://dividable.net/category/python/5").text
#print (category_res)

soup = BeautifulSoup(category_res, 'html.parser')
a_next_tag= soup.find_all("a", {"class": "next"}) # 次へがあるか確認するコード
print (a_next_tag)