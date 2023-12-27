import pandas as pd
import re
import jieba
import wordcloud
from wordcloud import WordCloud
import imageio

with open('7_en.txt', 'r', encoding='utf-8') as f:
    data = f.read()
# shape = imageio.v2.imread('shape.png')
stop_words = ["eat", "good","food","taste"] + list(wordcloud.STOPWORDS)
wc = WordCloud(
    height = 500,
    width = 500,
    background_color = 'white',
    scale = 15,
    font_path="SourceHanSansHK-Regular.otf",
    stopwords = stop_words
    # mask=shape
).generate(data)

wc.to_file("7_en.png")
