"""发送邮件"""
# 导入文本邮件格式库
from email.mime.text import MIMEText
# 导入混合邮件格式库
from email.mime.multipart import MIMEMultipart
# 导入发送邮件库
import smtplib
import os

class SendEmail(object):
    # def __init__(self):
    #     self.basePath = os.path.dirname(os.path.abspath("report.html"))
    #     self.filePath = os.path.join(self.basePath, 'reports', "report.html")
    #     print(self.filePath)

    def send_email(self):
        body = """测试发送邮件"""

        body2 = """
        <h1>测试报告</h1>
        <p>测试邮件发送功能</p>
        """
content = """测试发送带附件的邮件"""

# msg = MIMEText(body, 'plain', 'utf-8')
# msg2 = MIMEText(body2, 'html', 'utf-8')
msg = MIMEMultipart()
msg["From"] = '<Daisy' + '540224203@qq.com'
msg["To"] = '1584903008@qq.com, 540224203@qq.com'
msg["Subject"] = 'test send email'

body = MIMEText(content, 'plain', 'utf-8')
msg.attach(body)

f = open('123.txt', 'rb')
data = f.read()

att = MIMEText(data, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'   # 二进制流 声明上传的内容类型
att["Content-Disposition"] = 'attachment; filename = 123.txt'
msg.attach(att)



smtp = smtplib.SMTP('smtp.qq.com')  # 25
smtp.ehlo()
smtp.starttls()
# smtp2 = smtplib.SMTP_SSL('smtp.qq.com')  # 465
smtp.login('540224203@qq.com', 'acpkkzfdsdbdbcgc')
smtp.sendmail('540224203@qq.com', '1584903008@qq.com', msg.as_string())

f.close()


if __name__ == "__main__":
    SendEmail().send_email()
    print("发送成功")
