from pyspark.sql import SparkSession
from pyspark.sql.functions import col,udf
from pyspark.sql.types import ArrayType,StringType
import re
import csv
from urllib import request
from bs4 import BeautifulSoup as sp
import gzip
import time
import http.client
import os
from joblib import Parallel, delayed
import openpyxl



os.environ["PYSPARK_PYTHON"]="/Users/wangxiaoxuan/anaconda3/envs/py39/bin/python"
#get data_list
data =[]
workbook = openpyxl.load_workbook('/Users/wangxiaoxuan/Desktop/list.xlsx')
worksheet = workbook.active
for row in worksheet.iter_rows(min_row=2,max_row=2, values_only=True):
    data_json = {
        "name":"",
        "url":""
    }
    data_json["name"] = row[0]
    data_json["url"] = row[11]
    data.append(data_json)

print(len(data))

#the time of begining
start_time = time.time()
header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }


def write_csv(name, data):
    print("write_csv")
    with open(name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
def get_html(url):
    try:
        req = request.Request(url, headers=header)
        response = request.urlopen(req)
        compress = response.read()
        html = compress.decode('utf-8')
    except http.client.IncompleteRead as e:
        print("IncompleteRead exception occurred:", e)
        return None
    except Exception as e:
        print("exception occurred:", e)
        return None
    return sp(html, "html.parser")
def comments_parallel(comments_url, page_num):
    #print(page_num)
    url = comments_url + '?page=' + str(page_num)
    comments_result = get_detail_comments(url)
    # print("comments_result1:", comments_result)
    return comments_result
def get_detail_comments(url):
    soup = get_html(url)
    if soup is None:
        return None
    if (("Sorry, your search returned no results" in soup.text) or ("對不起，我們找不到符合您要求的食評" in soup.text) or (soup is None)):
        return None
    clients = soup.find_all('div', class_='sr2-review-list-container full clearfix js-sr2-review-list-container')
    comment_list = []
    for client in clients:
        data = {
            "time": "",
            "taste": "",
            "environment": "",
            "service": "",
            "hygiene": "",
            "indigestible": "",
            "comments": ""
        }
        # Get customer review time
        time = client.find('span', attrs={"itemprop": "datepublished"})
        data['time'] = time.text
        # Get customer meal scores
        scores = client.find_all('div', class_='subject')
        for index, score in enumerate(scores):
            if index == 0:
                taste = score.find_all("span", class_='or-sprite-inline-block common_yellowstar_desktop')
                data["taste"] = len(taste)
            if index == 1:
                environment = score.find_all("span", class_='or-sprite-inline-block common_yellowstar_desktop')
                data["environment"] = len(environment)

            if index == 2:
                service = score.find_all("span", class_='or-sprite-inline-block common_yellowstar_desktop')
                data["service"] = len(service)

            if index == 3:
                hygiene = score.find_all("span", class_='or-sprite-inline-block common_yellowstar_desktop')
                data["hygiene"] = len(hygiene)

            if index == 4:
                indigestible = score.find_all("span",
                                              class_='or-sprite-inline-block common_yellowstar_desktop')
                data["indigestible"] = len(indigestible)

        # Get customer comments
        comments = client.find_all('section', class_='review-container')
        for comment in comments:
            text = re.sub(r"^\d+.*", "", comment.text, flags=re.MULTILINE)
            data["comments"] = data["comments"] + text.replace('\n', "")
        data["comments"] = data["comments"].replace(" ", "")
        comment_list.append(data)
    return comment_list

def get_comments(name,url):
    comment_list = []
    comments_url = url + "/reviews"
    page_num = 2

    if comments_url is not None:
        comment_list = get_detail_comments(comments_url)
        #comments_result = get_detail_comments(comments_url)
        #print("第一个:", comments_result)
        while True:
            # results = Parallel(n_jobs=-1)(delayed(comments_parallel)(comments_url, page_num + i) for i in range(0, 30))
            # comments_result = results
            # for result in results:
            #     if result is not None:
            #         comment_list = comment_list + result
            #         #print("name:",name)
            #         #print("comment_list:",comment_list)
            # page_num += 30
            result = comments_parallel(comments_url,page_num)
            if result is None:
                break
            comment_list = comment_list + result
            page_num += 1
            print("comment_list:",comment_list)
            print(page_num)
    print("name:",name)
    write_csv("comments/"+name+".csv",comment_list)

for item in data:
    print(item)
    get_comments(item["name"],item["url"])

end_time = time.time()

# 计算执行时间
execution_time = end_time - start_time

# 打印执行时间
print("程序执行时间：", execution_time, "秒")

