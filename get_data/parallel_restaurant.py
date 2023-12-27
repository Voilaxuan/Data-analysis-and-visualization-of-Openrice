import gzip
import http.client
import mimetypes
import csv
from urllib import request
import requests
from bs4 import BeautifulSoup as sp
import re
import json
from sklearn.cluster import KMeans
from joblib import Parallel, delayed
class Openprice_spider():

    start_url = "https://www.openrice.com/zh/hongkong/restaurants"
    restaurant_list = []
    data_list = []
    district_id = ['districtId=-35243', 'districtId=-35242', 'districtId=1008', 'districtId=-35244', 'districtId=1001', 'districtId=1003', 'districtId=-9006', 'districtId=-9007', 'districtId=1005', 'districtId=1002', 'districtId=1011', 'districtId=1022', 'districtId=1017', 'districtId=1019', 'districtId=1025', 'districtId=1026', 'districtId=1004', 'districtId=1014', 'districtId=1023', 'districtId=1009', 'districtId=1018', 'districtId=1013', 'districtId=1024', 'districtId=1021', 'districtId=-9151', 'districtId=1020', 'districtId=1012', 'districtId=1027', 'districtId=1016', 'districtId=1015', 'districtId=1007', 'districtId=1010', 'districtId=2031', 'districtId=2016', 'districtId=2013', 'districtId=2019', 'districtId=2029', 'districtId=2010', 'districtId=2005', 'districtId=2011', 'districtId=2028', 'districtId=2008', 'districtId=-9008', 'districtId=2015', 'districtId=2009', 'districtId=2004', 'districtId=2007', 'districtId=2001', 'districtId=2002', 'districtId=2030', 'districtId=2020', 'districtId=2022', 'districtId=2027', 'districtId=2032', 'districtId=2021', 'districtId=2003', 'districtId=2006', 'districtId=2024', 'districtId=2026', 'districtId=2012', 'districtId=2025', 'districtId=3012', 'districtId=3013', 'districtId=3007', 'districtId=3009', 'districtId=3002', 'districtId=3008', 'districtId=3014', 'districtId=3011', 'districtId=3001', 'districtId=3021', 'districtId=3015', 'districtId=3019', 'districtId=3018', 'districtId=3022', 'districtId=3017', 'districtId=3010', 'districtId=3005', 'districtId=3003', 'districtId=3004', 'districtId=3016', 'districtId=3006', 'districtId=3020', 'districtId=-35260', 'districtId=-35259', 'districtId=-35276', 'districtId=4006', 'districtId=4002', 'districtId=4009', 'districtId=4001', 'districtId=4010', 'districtId=4004', 'districtId=4003', 'districtId=4011', 'districtId=4005']
    #district_id = ['districtId=-35243', 'districtId=-35242', 'districtId=1008']
    district_map = {
        "districtId=1001":"Sheung Wan",
"districtId=1002":"Mid-Levels",
"districtId=1003":"Central",
"districtId=1004":"North Point",
"districtId=1005":"The Peak",
"districtId=1007":"Shek O",
"districtId=1008":"Sai Wan",
"districtId=1009":"Sai Wan Ho",
"districtId=1010":"Stanley",
"districtId=1011":"Admiralty",
"districtId=1012":"Aberdeen",
"districtId=1013":"Chai Wan",
"districtId=1014":"Quarry Bay",
"districtId=1015":"Repulse Bay",
"districtId=1016":"Deep Water Bay",
"districtId=1017":"Happy Valley",
"districtId=1018":"Shau Kei Wan",
"districtId=1019":"Causeway Bay",
"districtId=1020":"Ap Lei Chau",
"districtId=1021":"Pok Fu Lam",
"districtId=1022":"Wan Chai",
"districtId=1023":"Taikoo",
"districtId=1024":"Heng Fa Chuen",
"districtId=1025":"Tai Hang",
"districtId=1026":"Tin Hau",
"districtId=1027":"Wong Chuk Hang",
"districtId=2001":"Kowloon City",
"districtId=2002":"Kowloon Tong",
"districtId=2003":"Kowloon Bay",
"districtId=2004":"To Kwa Wan",
"districtId=2005":"Tai Kok Tsui",
"districtId=2006":"Ngau Tau Kok",
"districtId=2007":"Shek Kip Mei",
"districtId=2008":"Tsim Sha Tsui",
"districtId=2009":"Ho Man Tin",
"districtId=2010":"Mong Kok",
"districtId=2011":"Yau Ma Tei",
"districtId=2012":"Yau Tong",
"districtId=2013":"Cheung Sha Wan",
"districtId=2015":"Hung Hom",
"districtId=2016":"Lai Chi Kok",
"districtId=2019":"Sham Shui Po",
"districtId=2020":"Wong Tai Sin",
"districtId=2021":"Tsz Wan Shan",
"districtId=2022":"San Po Kong",
"districtId=2024":"Lam Tin",
"districtId=2025":"Lei Yue Mun",
"districtId=2026":"Kwun Tong",
"districtId=2027":"Diamond Hill",
"districtId=2028":"Jordan",
"districtId=2029":"Prince Edward",
"districtId=2030":"Lok Fu",
"districtId=2031":"Meifoo",
"districtId=2032":"Rainbow",
"districtId=3001":"Sheung Shui",
"districtId=3002":"Tai Po",
"districtId=3003":"Yuen Long",
"districtId=3004":"Tin Shui Wai",
"districtId=3005":"Tuen Mun",
"districtId=3006":"Sai Kung",
"districtId=3007":"Sha Tin",
"districtId=3008":"Fanling",
"districtId=3009":"Ma On Shan",
"districtId=3010":"Sham Tseng",
"districtId=3011":"Lo Wu",
"districtId=3012":"Tai Wai",
"districtId=3013":"Fo Tan",
"districtId=3014":"Tai Wo",
"districtId=3015":"Kwai Fong",
"districtId=3016":"Lau Fau Shan",
"districtId=3017":"Tsing Yi",
"districtId=3018":"Tsuen Wan",
"districtId=3019":"Kwai Chung",
"districtId=3020":"Tseung Kwan",
"districtId=3021":"Lok Ma Chau",
"districtId=3022":"Ma Wan",
"districtId=-35242":"Sai Wan",
"districtId=-35243":"Sai Wan",
"districtId=-35244":"Sai Wan",
"districtId=-35259":"Tseung Kwan O",
"districtId=-35260":"Tseung Kwan O",
"districtId=-35276":"Tseung Kwan O",
"districtId=4001":"Lantau Island",
"districtId=4002":"Chek Lap Kok",
"districtId=4003":"Peng Chau",
"districtId=4004":"Cheung Chau",
"districtId=4005":"Lamma Island",
"districtId=4006":"Discovery Bay",
"districtId=4009":"Tung Chung",
"districtId=4010":"Tai O",
"districtId=4011":"Po Toi Island",
"districtId=-9006":"Central",
"districtId=-9007":"Central",
"districtId=-9008":"Tsim Sha Tsui",
"districtId=-9151":"Pok Fu Lam"}
    cuisine_map = {
        "西式":"Western Style",
    "日本菜":"Japanese Cuisine",
    "港式":"Hong Kong Style",
    "粵菜 (廣東)":"Cantonese Cuisine(Guangdong)",
    "粵菜(廣東)": "Cantonese Cuisine(Guangdong)",
    "多國菜":"International Cuisine",
    "意大利菜":"Italian Cuisine",
    "泰國菜":"Thai Cuisine",
    "台灣菜":"Taiwan Cuisine",
    "韓國菜":"Korean Cuisine",
    "川菜 (四川)":"Sichuan Cuisine",
    "川菜(四川)":"Sichuan Cuisine",
    "法國菜":"French Cuisine",
    "新加坡菜":"Singaporean Cuisine",
    "美國菜":"American Cuisine",
    "西班牙菜":"Spanish Cuisine",
    "越南菜":"Vietnamese Cuisine",
    "潮州菜":"Teochew Cuisine",
    "滬菜 (上海)":"Shanghai Cuisine",
    "滬菜(上海)":"Shanghai Cuisine",
    "印度菜":"Indian Cuisine",
    "英國菜":"British Cuisine",
    "地中海菜":"MediterraneanCuisine",
    "滇菜 (雲南)":"Dianella(Yunnan)",
    "滇菜(雲南)":"Dianella(Yunnan)",
    "中東菜":"Middle Eastern Cuisine",
    "馬來西亞菜":"Malaysian Cuisine",
    "墨西哥菜":"Mexican Cuisine",
    "澳洲菜":"Australian Cuisine",
    "京川滬":"Beijing, Sichuan and Shanghai",
    "德國菜":"German Cuisine",
    "土耳其菜":"Turkish Cuisine",
    "比利時菜":"Belgian Cuisine",
    "愛爾蘭菜":"Irish Cuisine",
    "東歐菜":"Eastern European cuisine",
    "京菜 (官府菜)":"Beijing Cuisine(Official Cuisine)",
    "京菜(官府菜)":"Beijing Cuisine(Official Cuisine)",
    "順德菜":"Shunde Cuisine",
    "葡國菜":"Portuguese Cuisine",
    "閩菜 (福建)":"Fujian Cuisine",
    "閩菜(福建)":"Fujian Cuisine",
    "客家菜":"Hakka cuisine",
    "印尼菜":"Indonesian cuisine",
    "湘菜 (湖南)":"Hunan Cuisine"
    }
    filename = 'data.csv'
    #有些用request方法获取的html不需要解压，有些需要解压，因此写了两个方法
    #爬虫获取html并解压
    def get_compress_html(self,url):
        req = request.Request(url, headers=self.header)
        response = request.urlopen(req)
        compress = response.read()
        html = gzip.decompress(compress).decode('utf-8')
        return sp(html, "html.parser")

    #爬虫获取html
    def get_html(self,url):
        try:
            req = request.Request(url, headers=self.header)
            response = request.urlopen(req)
            compress = response.read()
            html = compress.decode('utf-8')
        except http.client.IncompleteRead as e:
            print("IncompleteRead exception occurred:",e)
            return None
        except Exception as e:
            print("exception occurred:",e)
            return None
        return sp(html, "html.parser")

    #将数据写入csv
    def write_csv(self,name,data):
        with open(name,'w',newline='',encoding='utf-8') as file:
            writer = csv.DictWriter(file,fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def write_csv2(self,name,datas):
        with open(name,'w',newline='',encoding='utf-8') as file:
            writer = csv.DictWriter(file,fieldnames=datas[0][0].keys())
            writer.writeheader()
            for data in datas:
                writer.writerows(data)
    def paralle_restaurant(self,id,page_num):

        #url1 = "https://www.openrice.com/api/v1/pois?uiLang=zh&uiCity=hongkong&seoCategory=&callName=&page="
        url1="https://www.openrice.com/api/v1/pois?uiLang=zh&uiCity=hongkong&seoCategory=&callName=&sortBy=ORScoreDesc&"
        url = url1 + id +"&tabIndex=0&tabType=&page="+ str(page_num)
        print(url)
        req = requests.get(url, headers=self.header)
        data = req.text
        #print("data:",data)
        if ("對不起！出現錯誤了。" not in req.text):
            contents = json.loads(data)
            content = contents['searchResult']['paginationResult']['results']
            if len(content) == 0:
                return None
            results = []
            for item in content:
                element = {
                    "name": "",
                    "url": "",
                    "id":""
                }
                #print("reviewUrlUI",item['reviewUrlUI'])
                #print("nameUI",item['nameUI'])
                element['url'] = item['reviewUrlUI']
                element['name'] = item['nameUI']
                element['id'] = id
                results.append(element)
            print("page:",page_num,"results",results)
            return results
        else:
            return None


    #获取所有饭店
    def get_restaurant(self):
        # soup = self.get_compress_html(self.start_url)
        # restaurants = soup.find_all('a', class_='poi-name poi-list-cell-link')
        #
        # for restaurant in restaurants:
        #     data ={
        #         "name" : "",
        #         "url" : ""
        #     }
        #     data["name"] = restaurant.text.strip()
        #     data["url"] = "https://www.openrice.com" + restaurant.get("href")
        #
        #     self.restaurant_list.append(data)
        # print(self.restaurant_list)

        # page_count = 1
        # while page_count<300:
        #     element = {
        #         "name": "",
        #         "url": ""
        #     }
        #     url1 = "https://www.openrice.com/api/v1/pois?uiLang=zh&uiCity=hongkong&seoCategory=&callName=&page="
        #     url = url1 + str(page_count)
        #     print(url)
        #     req = requests.get(url1, headers=self.header)
        #     data = req.text
        #     if ("對不起！出現錯誤了。" not in req.text):
        #         page_count = page_count + 1
        #         contents = json.loads(data)
        #         content = contents['searchResult']['paginationResult']['results']
        #         for item in content:
        #             element['url'] = item['reviewUrlUI']
        #             element['name'] = item['nameUI']
        #             self.restaurant_list.append(element)
        #     else:
        #         break
        for id in self.district_id:
            results = Parallel(n_jobs=-1)(delayed(self.paralle_restaurant)(id,page_num) for page_num in range(1,18))

            if results is not None:
                for result in results:
                    if result is not None:
                        self.restaurant_list.extend(result)
        print("self.restaurant_list", self.restaurant_list)

    def parallel_detail_information(self,restaurant):
        data = {
            "name_chinese": "",
            "name_english": "",
            "location_chinese": "",
            "location_english": "",
            "district": "",
            "category": "",
            "sub_category":"",
            "price": "",
            "smile": "",
            "fine": "",
            "cry": "",
            "url":"",
            "district_map":""
        }
        #原来是评论的链接，去掉最后八个字符编程概要的链接
        #例如：
        #原：https://www.openrice.com/zh/hongkong/r-%E7%99%BE%E5%91%B3%E9%AE%AE%E8%BE%A3%E8%9F%B9%E5%B0%88%E9%96%80%E5%BA%97-%E8%A5%BF%E7%92%B0-%E6%B8%AF%E5%BC%8F-%E6%B5%B7%E9%AE%AE-r500499/reviews
        #去掉8个字符后变为https://www.openrice.com/zh/hongkong/r-%E7%99%BE%E5%91%B3%E9%AE%AE%E8%BE%A3%E8%9F%B9%E5%B0%88%E9%96%80%E5%BA%97-%E8%A5%BF%E7%92%B0-%E6%B8%AF%E5%BC%8F-%E6%B5%B7%E9%AE%AE-r500499
        url = "https://www.openrice.com" + restaurant["url"][:-8]
        data["url"] = url
        print("详细信息url:", url)
        soup = self.get_html(url)
        if soup is None:
            return None
        # get the location of restaurant
        locations = soup.find_all('a', attrs={'data-href': '#map'})
        for index, item in enumerate(locations):
            if index == 0:
                data['location_chinese'] = item.text.strip()
            elif index == 1:
                data['location_english'] = item.text.strip()

        # get the name of restaurant
        names = soup.select('span.name,div.smaller-font-name')
        for index, item in enumerate(names):
            if index == 0:
                data['name_chinese'] = item.text
            elif index == 1:
                data['name_english'] = item.text

        # get the evaluations of restaurant
        evaluations = soup.find('div', class_='header-smile-section')
        for index, evaluations in enumerate(evaluations.text.split()):
            if index == 0:
                data["smile"] = evaluations
            elif index == 1:
                data["fine"] = evaluations
            elif index == 2:
                data["cry"] = evaluations

        category = ""
        # get the district, pirce and category of restaurant
        elements = soup.find_all('div', class_='header-poi-base-info or-font-family')
        for element in elements:
            element = element.find_all('div')
            for index, item in enumerate(element):
                if index == 0:
                    data['district'] = item.text.strip("\r\n")
                    data['district_map'] = self.district_map[restaurant["id"]]
                elif index == 1:
                    data['price'] = item.text.strip("\n")
                elif index == 2:
                    categorys = item.find_all('a')
                    for index,category_item in enumerate(categorys):
                        if index == 0:
                            if category_item.text in self.cuisine_map:
                                data["category"] = self.cuisine_map[category_item.text]
                            else:
                                data["category"] = "other"
                        else:
                            category = category + '/' + category_item.text
        data['sub_category'] = category
        return data
    #获取饭店详细信息
    def get_detail_information(self):
        # for restaurant in self.restaurant_list:
        #     data = {
        #         "name_chinese": "",
        #         "name_english": "",
        #         "location_chinese": "",
        #         "location_english": "",
        #         "district": "",
        #         "category": "",
        #         "price": "",
        #         "smile": "",
        #         "fine": "",
        #         "cry": ""
        #     }
        #     url = restaurant["url"]
        #     soup = self.get_html(url)
        #     # get the location of restaurant
        #     locations = soup.find_all('a', attrs={'data-href': '#map'})
        #     for index, item in enumerate(locations):
        #         if index == 0:
        #             data['location_chinese'] = item.text.strip()
        #         elif index == 1:
        #             data['location_english'] = item.text.strip()
        #
        #     # get the name of restaurant
        #     names = soup.select('span.name,div.smaller-font-name')
        #     for index, item in enumerate(names):
        #         if index == 0:
        #             data['name_chinese'] = item.text
        #         elif index == 1:
        #             data['name_english'] = item.text
        #
        #     # get the evaluations of restaurant
        #     evaluations = soup.find('div', class_='header-smile-section')
        #     for index, evaluations in enumerate(evaluations.text.split()):
        #         if index == 0:
        #             data["smile"] = evaluations
        #         elif index == 1:
        #             data["fine"] = evaluations
        #         elif index == 2:
        #             data["cry"] = evaluations
        #
        #     category = ""
        #     # get the district, pirce and category of restaurant
        #     elements = soup.find_all('div', class_='header-poi-base-info or-font-family')
        #     for element in elements:
        #         element = element.find_all('a')
        #         for index, item in enumerate(element):
        #             if index == 0:
        #                 data['district'] = item.text
        #             elif index == 1:
        #                 data['price'] = item.text
        #             else:
        #                 category = category + '/' + item.text
        #     data['category'] = category
        #     self.data_list.append(data)
        results = Parallel(n_jobs=-1)(delayed(self.parallel_detail_information)(restaurant) for restaurant in self.restaurant_list)
        for result in results:
            if result is not None:
                self.data_list.append(result)

            #Get comments
            #comments_list = self.get_comments(restaurant)

            #Write comments into .csv file
            #self.write_csv2(restaurant["name"]+".csv",comments_list)

        #write restaurant information into .csv file
        print("self.data_list:",self.data_list)
        self.write_csv(self.filename,self.data_list)

    #获取评论详细信息
    def get_detail_comments(self,url):
        soup = self.get_html(url)
        if soup is None:
            return None
        if (("Sorry, your search returned no results" in soup.text) or (soup is None)):
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

    #获取所有评论页
    def get_comments(self,element):
        url = element['url']
        comment_list = []
        #The fist page of comments
        comments_url = url + "/reviews"
        page_num = 2
        if comments_url is not None:
            comments_result = self.get_detail_comments(comments_url)
            print("第一个:",comments_result)
            #Loop crawls all comment pages
            while len(comments_result[-1]) !=0:
                comment_list.extend(comments_result)
                #parallel k-means
                results = Parallel(n_jobs=-1)(delayed(self.comments_parallel)(comments_url,page_num+i)for i in range(0,30))
                print("其余：",results)
                comments_result = results
                page_num += 30
        comment_list.extend(comments_result)

        print(len(comment_list))
        comment_list = list(filter(None, comment_list))
        print(len(comment_list))
        print(comment_list)
        self.write_csv(element["name"] + ".csv", comment_list)

    def comments_parallel(self,comments_url,page_num):
        print(page_num)
        url = comments_url + '?page=' + str(page_num)
        comments_result = self.get_detail_comments(url)
        #print("comments_result1:", comments_result)
        return comments_result




def get_compression_type(data):
    mime = mimetypes.guess_type('filename',strict=False)
    if 'gzip' in mime:
        return 'gzip'
    elif 'bzip2' in mime:
        return 'bzip2'
    elif 'zip' in mime:
        return 'zip'
    elif 'tar' in mime:
        return 'tar'
    # 添加其他压缩方式的判断逻辑

    return None

element =  {
    'name' : 'test',
    'url' : 'https://www.openrice.com/zh/hongkong/r-%E8%8C%B6%E8%81%8A-%E6%97%BA%E8%A7%92-%E5%A4%9A%E5%9C%8B%E8%8F%9C-%E6%BC%A2%E5%A0%A1%E5%8C%85-r558545'

}
openprice_spider = Openprice_spider()
#get id, name and url of restaurant
openprice_spider.get_restaurant()
#get all detailed information except restaurant review
openprice_spider.get_detail_information()
