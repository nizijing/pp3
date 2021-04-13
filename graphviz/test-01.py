#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2021-02-06 18:23:57
# Author : zijing (zijing412@163.com)
###################################################
from graphviz import Digraph # 可以在实例化对象的时候设置样式
dot = Digraph(name="MyPicture", node_attr={"shape": "plaintext"}, format="png") # 也可以实例化之后, 设置这些样式
dot.graph_attr['rankdir'] = 'LR' 
dot.edge_attr.update(arrowhead='vee', arrowsize='2') # 然后开始画图
dot.node("Dog")
dot.node("Cat")
dot.edge("Dog", "Cat")

dot.view(filename="MyPicture")