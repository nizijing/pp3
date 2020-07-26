#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-07-26 14:33:42
# Author : zijing (zijing412@163.com)
###################################################
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from datetime import datetime

mail_sender_info = {
    'smtp_server': SMPT_SERVER,  
    'user': MAIL_USER,
    'port': SMPT_SERVER_PORT,
    'passwd': MAIL_PASSWD
    }

class SendMail(object):
    def __init__(self, sender_info = mail_sender_info, receiver=[], subject='test'):
        self.__user = sender_info['user']
        self.__receiver = receiver
        self.__passwd = sender_info['passwd']

        self.smtp = smtplib.SMTP_SSL(sender_info['smtp_server'], sender_info['port'])
        
        #self.smtp.connect(sender_info['smtp_server'], sender_info['port'])
        #self.smtp.ehlo()
        #self.smtp.starttls()
        self.smtp.login(self.__user, self.__passwd)
        self.__msg = MIMEMultipart('mixed')
        self.__msg['Subject'] = Header(subject,'utf-8')
        self.__msg['From'] = self.__user
        self.__msg['To'] = ";".join(receiver)
        self.__msg['date'] = str(datetime.now())

    def send_mail(self):
        self.smtp.sendmail(self.__user, self.__receiver, self.__msg.as_string())
        self.smtp.quit()

    def add_text(self, text):
        text_plain = MIMEText(text, 'plain', 'utf-8')
        self.__msg.attach(text_plain)

    def add_html(self, html):
        text_html = MIMEText(html, 'html', 'utf-8')
        text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
        self.__msg.attach(text_html)


def main():
    
    mail_receiver = ['abc@163.com']

    cmail = SendMail(mail_sender_info, mail_receiver, '测试')
    send_text = '测试'
    cmail.add_text(send_text)
    cmail.send_mail()

if __name__ == '__main__':
    main()
