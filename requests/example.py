#!/usr/bin/env python3
###################################################################
# File Name: gitlabapi2.py
# Author: zijing
# mail: xxx@xxx.cn
# Created Time: 2022-04-21 10:31:02
# version: 1.0
#==================================================================
import requests, json

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


if __name__ == '__main__':
    token='1W24fdmkUnwV_Y1LxLKv'
    projectUrl = 'http://gitlab.example.com/api/v4/projects?private_token=' + token
    getUrlResponse(projectUrl)
    postUrlResponse(projectUrl)