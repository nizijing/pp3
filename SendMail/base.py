#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-07-26 14:32:34
# Author : zijing (zijing412@163.com)
###################################################
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


class SendMail(object):
    def __init__(self, sender_info, receiver=[], subject=''):
        self.__user = sender_info['user']
        self.__receiver = receiver
        self.__passwd = sender_info['passwd']

        self.__msg = MIMEMultipart('mixed')
        self.__msg['Subject'] = subject
        self.__msg['From'] = self.__user
        self.__msg['To'] = ";".join(receiver)
        #        self.__msg['date'] = '2019-04-26'
        self.__smtp_server = sender_info['smtp_server']

    def send_mail(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.__smtp_server)
        smtp.login(self.__user, self.__passwd)
        smtp.sendmail(self.__user, self.__receiver, self.__msg.as_string())
        smtp.quit()

    def add_text(self, text):
        text_plain = MIMEText(text, 'plain', 'utf-8')
        self.__msg.attach(text_plain)

    def add_html(self, html):
        text_html = MIMEText(html, 'html', 'utf-8')
        text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
        self.__msg.attach(text_html)

def test_send_mail():
	mail_sender_info = {'smtp_server': 'smtp.mxhichina.com',
						'user': 'xxx@xxx.com',
						'passwd': 'xxxxxx'}
	mail_receiver = ['xxx@xxx.com', 'xxx@xxx.com', 'xxx@xxx.com']
	c_mail = SendMail(mail_sender_info, mail_receiver, '邮件主题')
	send_text = 'hello world\n'
	send_text += datetime.now().strftime('%Y-%m-%d')
	c_mail.add_text(send_text)
	c_mail.send_mail()
