from wordcloud import WordCloud

import MeCab

mecab = MeCab.Tagger()

f = open('filename.txt', 'r', encoding="utf-8")
#print(type(f))
print(f)
text = f.read()

print(mecab.parse( text ))

wakati = MeCab.Tagger("-Owakati")
#print(wakati.parse( text ))
words = wakati.parse( text )

wc = WordCloud(font_path='C:\Windows\Fonts\yumin.ttf', width=480, height=320, background_color="white")
wc.generate(words)
wc.to_file('wc2.png')

f.close()