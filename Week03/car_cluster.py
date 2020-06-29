from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd

data = pd.read_csv('car_data.csv', encoding='gbk')
train_x = data[["人均GDP", "城镇人口比重", "交通工具消费价格指数", "百户拥有汽车量"]]

# 规范化到[0,1]空间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv', index=False)

# 使用KMeans聚类
kmeans = KMeans(n_clusters=4)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)

# 合并聚类结果，插入到原数据中
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0: u'聚类结果'}, axis=1, inplace=True)

print(result)
result.to_csv("car_cluster_result.csv", index=False)
