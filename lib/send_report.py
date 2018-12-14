import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from conf import config

def send_mail():
    #编写邮件内容（Email邮件需要专门的MIME格式）
    msg = MIMEMultipart()
    body = MIMEText(config.body, 'plain', 'utf-8')
    msg.attach(body)
    #组装Email头（发件人，收件人，主题）
    msg["From"] = config.smtp_user
    msg["To"] = config.receive
    msg["Subject"] = config.smtp_subject
    #附件
    with open(config.report_file, "rb") as f:
        att_file = f.read()

    att = MIMEText(att_file, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = "attachment;filename=report.html"
    msg.attach(att)

    #连接smtp服器并发送邮件
    smtp = smtplib.SMTP(config.smtp_server)
    smtp.login(config.smtp_user, config.smtp_password)
    smtp.sendmail(config.smtp_user, config.receive, msg.as_string())