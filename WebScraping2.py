import requests
import pandas as pd
from bs4 import BeautifulSoup

columns = ["url", "title", "category"]
df = pd.DataFrame(columns=columns)

page_count = 1
category_res = ""
soup = ""
while True:
    print ("------------{} ページ目------------".format(page_count))
    category_res = requests.get("https://dividable.net/category/python/" + "page/" + str(page_count)).text
    soup = BeautifulSoup(category_res, 'html.parser') # BeautifulSoupの初期化
    post_tags = soup.select("div.post")
    for post_tag in post_tags:
        title = post_tag.select("h3")[0].text
        url = post_tag.select("a")[0].get("href")
        value = "テスト"
        se = pd.Series([url,title,value], columns)
        df = df.append(se, ignore_index=True)

        a_next_tag= soup.find_all("a", {"class": "next"})

    if a_next_tag:
        page_count += 1
        continue
    break

df.to_csv("result.csv")

print ("完了")