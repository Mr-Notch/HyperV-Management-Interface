from MainInterface import it_smtp_login_password
from MainInterface import it_smtp_login_user
from MainInterface import it_smtp_receiver_user
from MainInterface import it_smtp_sender_user
from MainInterface import it_smtp_server_address

from email.mime.text import MIMEText
import smtplib
def sendMail(title,context):
    # context must be str
    # title must be str
    msg = MIMEText(context,'plain','utf-8')
    msg['Subject'] = title
    msg['From'] = it_smtp_sender_user
    msg['To'] = ','.join(it_smtp_receiver_user)
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(it_smtp_server_address)
        smtpObj.login(it_smtp_login_user,it_smtp_login_password)
        smtpObj.sendmail(it_smtp_sender_user,it_smtp_receiver_user,msg.as_string())
        return True
    except smtplib.SMTPException as e:
        return e