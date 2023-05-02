#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   38-queue.py
@Time    :   2023/05/02 19:18:20
@Author  :   zijing
@Version :   1.0
@Site    :   https://none
@Desc    :   主线程生成队列，worker消费队列
             还有线程池的用法，可参考
             https://www.bilibili.com/video/BV11B4y1S7pB/?spm_id_from=333.788&vd_source=bd80b80e13fabcec3b17eb9c1f62604f
'''

import threading
import queue


def worker(q):
    while True:
        item = q.get()
        # if item is None:
        #    break
        print(item)
        q.task_done()


q = queue.Queue()
threading.Thread(target=worker, args=(q, ), daemon=True).start()


for i in range(10):
    q.put(i)


q.join()