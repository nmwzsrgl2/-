import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random
import SQL
import threading
# 验证邮箱是否存在
 
class Mail:
    def __init__(self, mail):
        self.mail = mail
    # 删除验证码过期
    def captcha_rm(self):
        SQL.captcha_rm(self.mail)    
    # 获取邮箱用户的用户名
    def check_SQL(self):
        try:
            mysql = SQL
            name = mysql.get_name_by_mail(self.mail)
            return name
        except:
            return self.mail
    def send_mail(self):
        # 生成随机验证码
        yzm = random.randint(10000, 99999)
        # 验证邮箱是否存在
        self.check_SQL()

        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "3533033347@qq.com"  # 用户名
        mail_pass = "evhmhftrnyjjcibg"  # 口令
        sender = '3533033347@qq.com'  # 发送者邮箱
        receivers = [self.mail,]  # 接收者邮箱
        mail_msg = f'''
        <div style="background-color:white;border: rgb(107, 107, 107);">
        <p>{self.check_SQL()}, 您好！</p>
        <p>您的验证码为:{yzm}</p>
        <p>请在3分钟内输入验证码完成验证，如非本人操作，请忽略本邮件。</p>
        </div>
    '''

        # 邮件内容设置
        message = MIMEText( mail_msg, 'html', 'utf-8')
        message['From'] = Header('Admin <3533033347@qq.com>')
        message['To'] = Header(self.check_SQL(), 'utf-8')
        message['Subject'] = Header(f"验证码:{yzm}", 'utf-8')
        print("验证码:",yzm,receivers[0])
        try:
            smtp = smtplib.SMTP_SSL(mail_host, 465)  # SMTP协议默认端口是25
            smtp.login(mail_user, mail_pass)
            smtp.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")

        except smtplib.SMTPException:
            print("Error: 无法发送邮件")   
        # 验证码存入数据库
        SQL.captcha_add(self.mail,yzm)
        # 验证码过期时间

    #多线程任务
    def run(self):
        self.captcha_rm()
        threading.Thread(target=self.send_mail).start()
        threading.Timer(180, self.captcha_rm).start()

