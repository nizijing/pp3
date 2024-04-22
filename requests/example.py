#!/usr/bin/env python3
###################################################################
# File Name: gitlabapi2.py
# Author: zijing
# mail: xxx@xxx.cn
# Created Time: 2022-04-21 10:31:02
# version: 1.0
#==================================================================
import requests, json

# 参考：https://blog.csdn.net/m0_43404934/article/details/122331463
# 防止访问https出告警
requests.packages.urllib3.disable_warnings()

def showRequestResult(jsonTest):
    for dictItem in json.loads(jsonTest):
        print("--" * 64)
        for key, val in dictItem.items():
            print(f"{key: <24}: {val}")


def getUrlResponse(url):
    headers = { "Content_type": "application/json" }
    req = requests.get(url, headers = headers, verify = False)
    showRequestResult(req.text)

def postUrlResponse(url):
    headers = { "Content_type": "application/json" }
    data = {"key": "val"}
    req = requests.post(url, data = data, headers = headers,  verify = False)
    showRequestResult(req.text)


def test1():
    #发送一个get请求并得到响应
    r = requests.get('https://www.baidu.com')

    print(r.status_code)
    print(type(r.cookies),r.cookies)
    print(type(r.headers),r.headers)
    print(type(r.url),r.url)
    print(type(r.history),r.history)
    
    print(type(r.text),r.text)
    print(type(r.content),r.content)
    print(r.json())
   


def test2():
    r = requests.post('https://www.baidu.com')
    r = requests.put('https://www.baidu.com')
    r = requests.delete('https://www.baidu.com')
    r = requests.head('https://www.baidu.com')
    r = requests.options('https://www.baidu.com')


def test3():
    r = requests.get('http://httpbin.org/get?name=germey&age=20')
    # 更优雅的写法
    data = {
        'name':'germey',
        'age':22
    }
    r = requests.get('http://httpbin.org/get',params=data)


if __name__ == '__main__':
    token='1W24fdmkUnwV_Y1LxLKv'
    projectUrl = 'http://gitlab.example.com/api/v4/projects?private_token=' + token
    getUrlResponse(projectUrl)
    postUrlResponse(projectUrl)
    








