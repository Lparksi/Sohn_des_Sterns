import smtplib
from email.mime.text import MIMEText
from email.header import Header
from nonebot.log import logger

from config import MAIL_SMTP_PORT, MAIL_SMTP_PASS, MAIL_SMTP_HOST, MAIL_SMTP_USER, USE_SMTP_MAIL

smtpObj = smtplib.SMTP()
smtpObj.connect(host=MAIL_SMTP_HOST, port=MAIL_SMTP_PORT)
smtpObj.login(user=MAIL_SMTP_USER, password=MAIL_SMTP_PASS)


def send(receiver: list or int, message: str, title: str = '星之子外发邮件') -> bool:
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = Header(f"星之子<{MAIL_SMTP_USER}>", 'utf-8')
    msg['To'] = Header(f'{receiver}<{receiver}>', 'utf-8')
    msg['Subject'] = Header(title, 'utf-8')

    try:
        smtpObj.sendmail(from_addr=MAIL_SMTP_USER, to_addrs=receiver,
                         msg=msg.as_string())
        return True
    except smtplib.SMTPException:
        logger.warn('[MAIL]邮件发送失败！')
