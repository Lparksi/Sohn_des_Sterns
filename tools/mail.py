import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.mxhichina.com"
mail_user = "bot@parksi.email"
mail_pass = "parksi2020."


def sendemail(toEmail, title, msg):
    sender = 'bot@parksi.email'
    receivers = [toEmail]

    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header("Parksi-Bot", 'utf-8')
    message['To'] = Header(receivers[0], 'utf-8')

    subject = title
    message['Subject'] = Header(subject, 'utf-8')


    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
