

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 读取餐厅数据
data = pd.read_csv("/Users/wangxiaoxuan/Desktop/kmean_data.csv")  # 假设数据保存在CSV文件中

# 提取特征向量
features = data[['location_lng', 'location_lat', 'smile_rate', 'mean_price']].values
print(data[['location_lng', 'location_lat', 'smile_rate', 'mean_price']].values)

# 执行K均值聚类
k_values = range(2, 10)  # 可尝试的K值范围
inertia_scores = []
silhouette_scores = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features)
    inertia_scores.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(features, kmeans.labels_))

# 使用肘部法确定K值
plt.figure(figsize=(10, 6))
plt.plot(k_values, inertia_scores, 'bo-')
plt.xlabel('K')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.grid(True)
plt.show()

# 使用轮廓系数法确定K值
plt.figure(figsize=(10, 6))
plt.plot(k_values, silhouette_scores, 'bo-')
plt.xlabel('K')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Coefficient Method')
plt.grid(True)
plt.show()


# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

data = pd.read_csv("/Users/wangxiaoxuan/Desktop/kmean_data.csv") 
# 餐厅数据
longitude = data[['location_lng', 'location_lat', 'smile_rate', 'mean_price']].values
latitude = data[['location_lat']].values
price = data[['smile_rate']].values
rating = data[['mean_price']].values


# 将经度和纬度合并为位置特征
locations = np.column_stack((longitude, latitude))
print(locations)

# 将位置、价格和好评率作为特征矩阵
features = np.column_stack((locations, price, rating))
#print("features",features)

# 归一化特征
scaler = MinMaxScaler()
normalized_features = scaler.fit_transform(features)

# 使用K均值算法进行聚类
k = 5  # 分类数量
kmeans = KMeans(n_clusters=k, random_state=0).fit(normalized_features)

# 获取聚类的标签
labels = kmeans.labels_

#获得中心聚点
centroids = kmeans.cluster_centers_

# 可视化分类结果
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

for loc, p, r, c in zip(locations, price, rating, labels):
    ax.scatter(loc[0]**loc[0]+loc[1]**loc[1], r,p , c='r' if c == 0 else 'g' if c == 1 else 'b' if c == 2 else 'y' if c == 3 else 'purple' , marker='o')
ax.set_xlabel('location')
ax.set_ylabel('price')
ax.set_zlabel('rating')
plt.title('Restaurant Clustering')
plt.legend()
plt.savefig('kmeans_clusters_5.png')
plt.show()






