# -- coding: utf-8 --
import smtplib
import Injector
from email.mime.text import MIMEText


def mailSender(receiver, content, vmname, starttime, maturitytime, vmconfig, connectconfig):

    smtp_srv = Injector.smtp_server
    smtp_passwd = Injector.smtp_server_password
    mail_sender = Injector.smtp_sender
    mail_login_user = Injector.smtp_login_user

    # msg_create_vm = "虚拟机名称: " + vmname + "\n" + "开通账户: " + receiver + "\n" + "开通日期: " + Injector.nowTime() + "\n" + "到期时间: " + maturitytime + "\n" + "配置参数: " + vmconfig + "\n" + "连接信息: " + connectconfig
    # msg_delete_vm = "虚拟机名称: "+vmname+"\n"+"开通账户: "+receiver+"\n"+"已删除文件: 是"
    # msg_finish_maturitytime="虚拟机名称: "+vmname+"\n"+"开通账户: "+receiver+"\n"+"开通日期: "+starttime+"\n"+"到期时间: "+maturitytime+"\n"+"到期保留: "+Injector.maturity_keep_time+" 天"
    msg_create_vm = "虚拟机名称: " + vmname + "\n" + "开通账户: " + receiver[0] + "\n" + "开通日期: " + Injector.nowTime() + "\n" + "到期时间: " + maturitytime + "\n" + "配置参数: " + vmconfig + "\n" + "连接信息: " + connectconfig
    msg_delete_vm = "虚拟机名称: "+vmname+"\n"+"开通账户: "+receiver[0]+"\n"+"已删除文件: 是"
    msg_finish_maturitytime="虚拟机名称: "+vmname+"\n"+"开通账户: "+receiver[0]+"\n"+"开通日期: "+starttime+"\n"+"到期时间: "+maturitytime+"\n"+"到期保留: "+Injector.maturity_keep_time+" 天"

    if content == "Create-VM":
        msg = MIMEText(msg_create_vm, 'plain', 'utf-8')
        msg['Subject'] = '新建虚拟机成功 - HMI'
        msg['From'] = mail_sender
        msg['To'] = receiver[0]
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(smtp_srv)
            smtpObj.login(mail_login_user, smtp_passwd)
            smtpObj.sendmail(mail_sender, receiver, msg.as_string())
            return True
        except smtplib.SMTPException as e:
            return e
    elif content == "Delete-VM":
        msg = MIMEText(msg_delete_vm, 'plain', 'utf-8')
        msg['Subject'] = '删除虚拟机成功 - HMI'
        msg['From'] = mail_sender
        msg['To'] = receiver[0]
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(smtp_srv)
            smtpObj.login(mail_login_user, smtp_passwd)
            smtpObj.sendmail(mail_sender, receiver, msg.as_string())
            return True
        except smtplib.SMTPException as e:
            return e
    elif content == "Finish-MaturityTime":
        msg = MIMEText(msg_finish_maturitytime, 'plain', 'utf-8')
        msg['Subject'] = '虚拟机已到期 - HMI'
        msg['From'] = mail_sender
        msg['To'] = ','.join(receiver)
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(smtp_srv)
            smtpObj.login(mail_login_user, smtp_passwd)
            smtpObj.sendmail(mail_sender, receiver, msg.as_string())
            return True
        except smtplib.SMTPException as e:
            return e

# mailSender(Injector.smtp_receiver_user,"Finish-MaturityTime","test","2021-2-16","2021-3-16","2C+2G","3389->11092, 25565->20000")