#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-05-05 15:47:32
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
import paramiko
 
transport = paramiko.Transport(('192.168.213.104', 22))
transport.connect(username='root', password='110054')
 
sftp = paramiko.SFTPClient.from_transport(transport)
 
# upload
sftp.put('README.md', '/tmp/README.md')
 
# download
sftp.get('/tmp/README.md', 'readme.txt')
 
transport.close()