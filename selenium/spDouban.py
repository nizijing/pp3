#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-07-26 14:27:06
# Author : zijing (zijing412@163.com)
###################################################
from selenium import webdriver

# open 
browser = webdriver.Chrome()

# input url
browser.get('https://movie.douban.com/')

# 找到输入框元素的id，输入中国机长
kword = '中国机长'
browser.find_element_by_id('inp-query').send_keys(kword)

# 找到搜索元素的id，点击
browser.find_elements_by_css_selector('#db-nav-movie > div.nav-wrap > div > div.nav-search > form > fieldset > div.inp-btn > input[type="submit"]')[0].click()

kword = '美国队长'
sinput = browser.find_element_by_id('inp-query')
sinput.clear()
sinput.send_keys(kword)
browser.find_elements_by_css_selector('#db-nav-movie > div.nav-wrap > div > div.nav-search > form > fieldset > div.inp-btn > input[type="submit"]')[0].click()