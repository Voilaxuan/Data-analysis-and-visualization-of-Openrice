如欲获取相关报告、PPT及详细指南，请联系作者:1716207520@qq.com。

If you want to get relevant report, PPT and detailed guideline, please contact author: 1716207520@qq.com.

This project is build based on pyspark & parallel and divided into 3 parts - obtain data of OpenRice, data transformation, data visulization.
1. Obtain data from OpenRice
   
(1) Run parallel_resautaurant.py in get_data folder and the data obtained are as follows which is saved in /dataset/data.csv:
![1](https://github.com/Voilaxuan/Data-analysis-and-visualization-of-Openrice/assets/42267315/5aae4790-3ade-4e76-90e2-b59283d650e7)

(2) Run review_pyspark.py in get_data folder to obtain comments and the data is saved in /dataset/comments
<img width="480" alt="Picture1" src="https://github.com/Voilaxuan/Data-analysis-and-visualization-of-Openrice/assets/42267315/89157ef2-1ced-420c-8c69-1d11ba0cabe4">

2. Data transformation

 (1) run call_google_map_api.py to get longitude and latitude of each restaurant.
 
 (2) run smile_rate.py to get applause rate of each restaurant.
 
 (3) run k-means.py to get clustering result.
![Picture1](https://github.com/Voilaxuan/Data-analysis-and-visualization-of-Openrice/assets/42267315/a0ff171b-bc68-4aea-aef5-95ffc84db9a8)

4. Data visulization

(1) Word cloud

![6_en](https://github.com/Voilaxuan/Data-analysis-and-visualization-of-Openrice/assets/42267315/b8087417-5a2b-4c97-b177-9b4918bed514)

(2) other chart

![bar](https://github.com/Voilaxuan/Data-analysis-and-visualization-of-Openrice/assets/42267315/df9dbb35-ba09-4dd1-b9da-71dfb789158e)

![box](https://github.com/Voilaxuan/Data-analysis-and-visualization-of-Openrice/assets/42267315/dbf41fc1-91b9-4c5f-83e8-279aa2cd7429)

![Pair](https://github.com/Voilaxuan/Data-analysis-and-visualization-of-Openrice/assets/42267315/fb594db8-ac1e-42aa-ae93-70d31cdca205)

![groupbar2](https://github.com/Voilaxuan/Data-analysis-and-visualization-of-Openrice/assets/42267315/0c31dc58-90e4-4ed9-be9c-71a0f83ab210)

![Scatter_Plot2](https://github.com/Voilaxuan/Data-analysis-and-visualization-of-Openrice/assets/42267315/4130012f-7690-447a-b318-e9706dae7112)









