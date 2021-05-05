#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-05-05 15:43:09
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.213.104', username = 'pukka', key_filename= 'D:\\etc\\key\\id_dsa', port='22')
cmd = 'pwd'
stdin,stdout,stderr = ssh.exec_command(cmd)
result = stdout.read()
print(stderr.read().decode('utf-8'))
print(result)
print(result.decode('utf-8'))
ssh.close()