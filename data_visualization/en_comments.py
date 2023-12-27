import pandas as pd
import re
import jieba
from wordcloud import WordCloud
#漁獲浜燒

data = pd.read_csv('data.csv')
comment_data = data['comments']
comment_data = comment_data[:300]

def is_valid(char):
    pattern = re.compile(r'[\u4e00-\u9fa5a-zA-Z0-9,.。，!?\s]')
    if re.match(pattern, char):
        return True
    else:
        return False

def check_comments(text):
    comment_text=''
    for char in text:
        if is_valid(char):
            comment_text += char
    return comment_text

filename = "data.txt"
all_valid_comments = []
for line in comment_data:
    valid_comments=''
    valid_comments += check_comments(str(line))
    all_valid_comments.append(valid_comments)

file = open(filename, "w")
file.write(str(all_valid_comments).replace(r'\r',''))
file.close()

