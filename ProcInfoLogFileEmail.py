"""
Design automation script which accept directory name and mail id from user and create log
file in that directory which contains information of running processes as its name, PID,
Username. After creating log file send that log file to the specified mail.

Usage : ProcInfoLogFileEmail.py Demo shubhamteli496@gmail.com
Demo is name of Directory.
shubhamteli496@gmail.com is the mail id.
"""
import smtplib
import sys
import time;
from email.encoders import encode_base64
from mimetypes import guess_type

import psutil;
import os;
import checkInternet;
from email.mime.text import MIMEText;
from email.mime.base import MIMEBase;
from email.mime.multipart import MIMEMultipart;

def mailSender(fname,emailId,time):
    try:
        fromadd = "shubhamteli0310@gmail.com";
        toadd = emailId;

        msg=MIMEMultipart();
        msg['From']=fromadd;
        msg['To']=toadd;

        body='''
         Hello %s
         Please find attached log of Running processes 
         log file created at %s 
         
         Thanks & Regards,
         Shubham
         '''%(emailId,time);

        subject=''' Process log generated at %s'''%time;

        msg['Subject']=subject;
        msg.attach(MIMEText(body,'plain'));


        mimetype, encoding = guess_type(fname);
        mimetype = mimetype.split('/', 1);
        fp = open(fname, 'rb');
        attachment = MIMEBase(mimetype[0], mimetype[1]);
        attachment.set_payload(fp.read());
        fp.close();
        encode_base64(attachment);
        attachment.add_header('Content-Disposition', 'attachment',filename=os.path.basename(fname));
        msg.attach(attachment);


        s=smtplib.SMTP('smtp.gmail.com',587);
        s.starttls();
        s.login(fromadd,"@AbhyassTapalPatra9806#");
        text=msg.as_string();
        s.sendmail(fromadd,toadd,text);
        s.quit();
        print("Log file successfully sent through email.")
    except Exception as E:
        print("Unable to send email",E);


def processLogger(dirName):

    if not os.path.exists(dirName):
        os.mkdir(dirName);

    listProcess=[];
    logfile="RunningProcesses.txt";
    log_path=os.path.join(dirName,logfile)
    with open(log_path,'w') as fobj:
        separator="-"*80;
        fobj.write(separator + "\nProcess Logger : " + str(time.ctime()) + "\n" + separator + "\n" );

        for pro in psutil.process_iter():
            try:
                pinfo=pro.as_dict(attrs=['pid','name','username']);
                listProcess.append(pinfo);
            except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
                pass;
        for element in listProcess:
            fobj.write("%s\n"%element);
        print("Log file generated successfully at %s location"%log_path);

        connected=checkInternet.check_internet();
        if not connected:
            print("Not Connected to Internet.");
            exit(0);
        else:
            return log_path;

def main():
      try:
         log_path=processLogger(str(sys.argv[1]));
         mailSender(log_path,str(sys.argv[2]),time.ctime());

      except Exception as E:
          print("Exception occured: ",E);


if __name__ == "__main__":
    main();
