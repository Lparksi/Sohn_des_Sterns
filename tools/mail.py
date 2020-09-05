import smtplib
from email.header import Header
from email.mime.text import MIMEText

mail_host = "smtp.mxhichina.com"
mail_user = "bot@parksi.email"
mail_pass = "parksi2020."


def sendemail(toEmail, title, msg):
    sender = 'bot@parksi.email'
    receivers = [toEmail]

    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header("Parksi-Bot<bot@parksi.email>", 'utf-8')
    message['To'] = Header(receivers[0], 'utf-8')

    subject = title
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPRecipientsRefused as e:
        return e
    else:
        return 0
