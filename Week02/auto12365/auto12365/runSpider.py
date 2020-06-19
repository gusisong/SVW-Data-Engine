# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2020/6/19 15:47
# @Author: Gu Sisong

import os

print('run auto12365 spider')
os.system('scrapy crawl complaint -o complaint.csv')