import os
import smtplib
import shutil
from pathlib import Path
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime

linux = True


# Read counter
def readcounter():
    # read counter
    path = Path(__file__).parent.parent / "testconf/counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    return data


# Read and Update counter
def readAndUpdateCounter():
    # read counter
    path = Path(__file__).parent.parent / "testconf/counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    # update counter
    newCounter = str(data + 1)
    # write new counter
    f.seek(0)
    f.write(newCounter)
    f.truncate()
    f.close()
    return newCounter


# Read current date
def readdate():
    return str(datetime.today().strftime('%Y-%m-%d'))


# Send mail
def sendmail(senderemail, senderpassword, receiversemail, mailsubject, mailbody, attachedfilepath, bccemail=''):
    # Mail content, format, encoding
    message = MIMEMultipart()
    message['From'] = senderemail
    message['To'] = receiversemail
    message['Subject'] = Header(mailsubject, 'utf-8')
    if bccemail:
        message['Bcc'] = bccemail
    message.attach(MIMEText(mailbody))

    # build the attachment
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(open(attachedfilepath, 'rb').read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attachedfilepath))
    message.attach(attachment)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(senderemail, senderpassword)
        server.send_message(message)
        # server.sendmail(senderemail, receivers, message.as_string())
        print("Send email successfully!!!")
        server.close()
    except smtplib.SMTPException:
        print("Failed to send mail!!!")


# Delete Folder and its content except last n number of dirs
def deldir(num_of_dir):
    basedir = Path(__file__).resolve().parent.parent
    dirname = "ReportAllure"
    dirpath = os.path.join(basedir, dirname)
    # print(dirPath)
    # dirList = [f for f in sorted(os.listdir(dirPath))]
    dirlist = [os.path.join(dirpath, f) for f in sorted(os.listdir(dirpath))]
    dirlist = dirlist[:len(dirlist) - num_of_dir]
    # print(dirList)
    for folder in dirlist:
        try:
            shutil.rmtree(folder)
            # print('delete: ' + delDir)
        except OSError as e:
            print("Error: %s : %s" % (folder, e.strerror))
        # print('dir deleted')


# Delete file except last n number of files
def delfile(num_of_file):
    basedir = Path(__file__).resolve().parent.parent
    dirname = "ReportHtml"
    dirpath = os.path.join(basedir, dirname)
    filelist = [os.path.join(dirpath, f) for f in sorted(os.listdir(dirpath))]
    filelist = filelist[:len(filelist) - num_of_file]
    # print(fileList)
    for file in filelist:
        os.remove(file)


def keepreports(number):
    deldir(number)
    delfile(number)


def sendemail(sender, password, receivers, filename):
    bccemail = ''
    emailsubject = 'Test Report'
    emailbody = "Dear Sir, Please check this report."
    attachedfilepath = Path(__file__).parent.parent / f"ReportHtml/report_{filename}.html"
    sendmail(sender, password, receivers, emailsubject, emailbody, attachedfilepath, bccemail)


def connectionOff():
    if linux:
        # connectionOff = "nmcli networking off"
        off = "nmcli r wifi off"
        os.system(off)
    else:
        off = "netsh wlan disconnect"
        os.system(off)


def connectionOn():
    if linux:
        # connectionOn = "nmcli networking on"
        on = "nmcli r wifi on"
        os.system(on)
    else:
        on = 'netsh wlan connect name="network_name"'
        os.system(on)
