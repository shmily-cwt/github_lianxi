#coding:utf-8
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import HTMLTestRunner
import unittest
import smtplib
import time
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

# suit = unittest.TestSuite()
# suit.addTest(testBLPC.BLtest("test_bl_index"))
#定义发送邮件方法
def send_email(now_file):
    #定义发送邮箱服务器
    mail_server = "mail.bl.com"
    #定义发送者的账号和密码
    user = 'CWT62'
    password = 'bl@123456'
    #定义发送者的邮箱
    sender = 'WenTao.Chen@bl.com'
    #定义接收者的邮箱
    #receiver = ['JiaJun.Tang@bl.com','Li.Huang@bl.com','Lian.Liu@bl.com']
    receiver = ['Li.Huang@bl.com']
    #定义发送主题
    subject = "自动化测试报告"
    #定义发送文件
    #print now_file
    send_file = open(now_file,'rb').read()
#发送文件形式
#     att = MIMEText(mail_body,'base64','utf-8')
#     att["Content-type"] = 'application/octet-stream'
#     att["Content-Disposition"] = 'attachment; filename = "result.html"'
#     msgRoot = MIMEMultipart('related')
#     msgRoot['Subject'] = subject
#     msgRoot.attach(att)
    
#直接以文本形式发送
    msg = MIMEText(send_file,'html','utf-8')
    msg['Subject'] = Header(subject,'utf-8')
    #链接邮箱发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(mail_server)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
#找到最新的测试报告
def now_report(result_file):
    #返回result_file文件夹中所有文件和文件夹
    lists = os.listdir(result_file)
    #对返回的lists中文件和文件夹按照时间进行排序
    lists.sort(key = lambda fn: os.path.getmtime(result_file+"\\"+fn))
    now_file = os.path.join(result_file,lists[-1])
#     print now_file
#     print type(now_file)
    return now_file
    


if __name__ == "__main__":
    test_dir = "D:\\Program Files\\eclipseworkspace\\BL_H5\\src\\test_case"
    report_dir = "D:\\Program Files\\eclipseworkspace\\BL_H5\\src\\report"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    ISOTIMEFORMAT='%Y-%m-%d %H_%M_%S' #设置时间格式
    #返回系统当前时间并转换成str类型
    now_time = time.strftime(ISOTIMEFORMAT,time.localtime())
    fp = open(report_dir +'\\'+now_time+'report.html' , 'wb')
    
    #runner = unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp,
                                           title = '百联登录测试报告',
                                           description = '用例执行情况')
    #runner.run(suit)
    runner.run(discover)
    fp.close()
    
    now_report = now_report(report_dir)
    send_email(now_report)
    