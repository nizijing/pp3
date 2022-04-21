import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def send_mail():
    sender = 'sender@abc.com'
    receivers = ['recv@abc.com']
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = ','.join(receivers)
    message['Cc'] = 'copyer@boomingtech.com'  # 抄送
    message['Subject'] = Header("邮件标题", 'utf-8')
    message.attach(MIMEText("邮件内容", 'plain', 'utf-8'))

    attachment = MIMEText(open(CSV_PATH, 'rb').read(), 'base64', 'gbk')
    attachment["Content-Type"] = "application/octet-stream"
    attachment["Content-Disposition"] = "attachment; filename='xxx.csv'" 
    message.attach(attachment)
    
    smtpObj = smtplib.SMTP('smtphz.qiye.163.com')
    # smtpObj.set_debuglevel(True)  # debug
    smtpObj.starttls()  # 加密传输
    smtpObj.login(sender, 'xxxxxxxxxxxx')  # 建议写客户端授权码，从网页登录邮箱，设置 --> 客户端设置 --> 生成新的授权密码
    smtpObj.sendmail(sender, receivers, message.as_string())