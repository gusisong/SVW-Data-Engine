# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class Auto12365Pipeline(object):
    def process_item(self, item, spider):

        # 拆分字符串，去空值
        item["典型问题"] = item["典型问题"][0].split(',')
        item["典型问题"] = [i for i in item["典型问题"] if i != '']

        # 导入问题编码
        csv_file = 'problem.csv'
        reader = csv.reader(open(csv_file, encoding='UTF_8'))
        dict_unit = {}
        dict_issue = {}

        # 构建字典
        for row in reader:
            dict_unit[row[2]] = row[1]
            dict_issue[row[4]] = row[5]

        # 批量替换问题描述
        for seq in range(0, len(item["典型问题"])):
            i = item["典型问题"][seq]
            item["典型问题"][seq] = str(i).replace(i[0], dict_unit[i[0]]).replace(i[1:], dict_issue[i[1:]])

        # print(item["典型问题"])
        return item
