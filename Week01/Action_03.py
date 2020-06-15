# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2020/6/15 21:57
# @Author: Gu Sisong

"""
Action3: 对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem类型 => 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数
哪个品牌的平均车型投诉最多
"""

import pandas as pd

# 数据加载
source = pd.read_csv('car_complain.csv')

# 数据预处理,拆分problem类型 => 多个字段
source = source.drop('problem', 1).join(source.problem.str.get_dummies(','))
tags = source.columns[7:]

# 按品牌统计投诉总数
df = source.groupby(['brand'])['id'].agg(['count'])
df2 = source.groupby(['brand'])[tags].agg(['sum'])
df2 = df.merge(df2, left_index=True, right_index=True, how='left')
df2.reset_index(inplace=True)
df2 = df2.sort_values('count', ascending=False)
print(df2)

# 按车型统计投诉总数
df3 = source.groupby(['car_model'])['id'].agg(['count'])
df4 = source.groupby(['car_model'])[tags].agg(['sum'])
df4 = df3.merge(df4, left_index=True, right_index=True, how='left')
df4.reset_index(inplace=True)
df4 = df4.sort_values('count', ascending=False)
print(df4)

# 按指定的问题类型排序
df_new = source.groupby(['brand'])['A11'].agg(['count'])
print(df_new.sort_values('count',ascending=False))