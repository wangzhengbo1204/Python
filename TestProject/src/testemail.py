#-*- coding:utf-8 -*-
'''
Created on 2011-11-30

@author: GFTOwenWang
'''
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from gftdata.share.utility.exc import exception2unicode
from gftdata.share.utility.log import Log
from gftdata.share.utility.appconfig import AppCon
import smtplib
import traceback
import StringIO
from gftdata.share.utility.emailutil import send_message, send_error


################################################################################
#                            Global Settings                                   #
################################################################################
SERVER = 'smtp.gftchina.com'
user = 'Data_Sender@gftchina.com'
passwd = 'datasender123'

From = "Data_Sender@gftchina.com"
To = AppCon.get_request("Special", "Mail_List")
#To = [str(to) for to in To]

#To = "wangzhengbo@gftchina.com-zhangyue@gftchina.com".split("-")
#To = ["qinyang@gftchina.com","wangzhengbo@gftchina.com","zhangwei@gftchina.com","zhangyue@gftchina.com"]

process_name = "Fetcher"
dict_msg_level = {0:'DEBUG', 1:'INFO', 2:'WARNING', 3:'ERROR', 4:'CRITICAL'}

def traceback_message():
    s = StringIO.StringIO()
    traceback.print_exc(file=s)
    return s.getvalue()

def email_error(ex, msg='', level=3, tolog=True):
    if tolog:
        Log.error(msg, None, ex)
    ex_msg = exception2unicode(ex)
    if msg:
        msg = u"%s\n%s" % (msg, ex_msg)
    else:
        msg = ex_msg
    tb_msg = traceback_message()
        
    message = """
    %s\n\n
    %s\n
    %s\n
    %s\n
    """ % (msg, '-'*20, tb_msg, '-'*20)
    
    email_message(message, level)

def email_message(msg, level=1):
    subject = ''
    if len(msg.strip()) > 30:
        subject = (msg.strip())[0:30]
    else:
        subject = msg.strip()
    
    subject = u"%s-%s:%s" % (process_name, dict_msg_level[level], subject)
    send_email(subject, msg)

def send_email(subject, message, attach=False):
    if isinstance(subject, unicode):
        subject = subject.encode('utf-8')
    
    if isinstance(message, unicode):
        message = message.encode('utf-8')
        
    sendEmail(To, From, subject, message, attach)

################################################################################
def sendEmail(TO, FROM, SUBJECT, MESSAGE, ATTACH=False):   
################################################################################
    # Determine type of email
    if ATTACH != False: msg = MIMEMultipart()
    else: msg = MIMEText(MESSAGE) 
    
    # this works for both types of emails
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = TO

    if ATTACH != False: 
        # That is what u see if dont have an email reader:
        msg.preamble = 'Multipart massage.\n'
    
        # This is the textual part:
        part = MIMEText("Hello I'm sending an email from a python program")
        msg.attach(part)
    
        # This is the binary part(The Attachment):
        part = MIMEApplication(open(ATTACH, "rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=ATTACH)
        msg.attach(part)

    s = smtplib.SMTP(SERVER)
    s.login(user, passwd)
    list_to = TO.split(";")
    s.sendmail(FROM, list_to, msg.as_string())
    s.quit()

#try:
#    a=1/0
#    print a
#except Exception as ex:
#    email_error(ex, "only test email")
#    
def func1():
    try:
        a=1/0
    except Exception as ex:
        send_error(ex=ex, attach=r"d:\a.txt")

if __name__ == '__main__':
    func1()
    
    
