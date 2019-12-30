"""
Accept Directory name from user and delete all duplicate files from the specified directory by
considering the checksum of files.
Create one Directory named as Marvellous and inside that directory create log file which
maintains all names of duplicate files which are deleted.
Name of that log file should contains the date and time at which that file gets created.
Accept duration in minutes from user and perform task of duplicate file removal after the specific
time interval.
Accept Mail id from user and send the attachment of the log file.
Mail body should contains statistics about the operation of duplicate file removal.
Mail body should contains below things :
Starting time of scanning
Total number of files scanned
Total number of duplicate files found
Consider below command line options for the gives script
DupFileRemovalEmailLog.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
- DupFileRemovalEmailLog.py
Name of python automation script
- E:/Data/Demo
Absolute path of directory which may contains duplicate files
- 50
Time interval of script in minutes
- marvellousinfosystem@gmail.com
Mail ID of the receiver
"""
import smtplib
import sys;
import os;
from datetime import datetime

from email.encoders import encode_base64
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mimetypes import guess_type

import Checksum;
import schedule;
import time;
import checkInternet;


def mailSender(log_path, emailId,starTime,totalFiles,dupFiles,fileGenTime):
    try:
        fromadd = "shubhamteli0310@gmail.com";
        toadd = emailId;

        msg = MIMEMultipart();
        msg['From'] = fromadd;
        msg['To'] = toadd;

        body = '''
         Hello %s
         Please find attached log file of duplicate files
         Starting time of scanning: %s
         Total number of files scanned : %d
         Total number of duplicate files found: %d 
         
         Thanks & Regards,
         Shubham
         ''' % (emailId, starTime,totalFiles,dupFiles);

        subject = ''' Process log generated at %s''' %fileGenTime;

        msg['Subject'] = subject;
        msg.attach(MIMEText(body, 'plain'));

        mimetype, encoding = guess_type(log_path);
        mimetype = mimetype.split('/', 1);
        fp = open(log_path, 'rb');
        attachment = MIMEBase(mimetype[0], mimetype[1]);
        attachment.set_payload(fp.read());
        fp.close();
        encode_base64(attachment);
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(log_path));
        msg.attach(attachment);


        s = smtplib.SMTP('smtp.gmail.com', 587);
        s.starttls();
        s.login(fromadd, "@AbhyassTapalPatra9806#");
        text = msg.as_string();
        s.sendmail(fromadd, toadd, text);
        s.quit();
        print("Log file successfully sent through email.")
    except Exception as E:
        print("Unable to send email", E);

def DelDups(dic,dirName):
    results = list(filter(lambda x : len(x) > 1 ,dic.values()));

    if len(results) > 0:
        print("Duplicate files found and deleted!!!!");

        fname= datetime.now().strftime('mylogfile_%Y-%m-%d_%H-%M-%S.txt')
        log_path = os.path.join(dirName, fname)
        with open(log_path,'w') as fobj:
            fobj.write("Following Duplicate files are deleted successfully!!!!");
            fobj.write("\n" + "---" * 30);
            for result in results:
                fcnt=0;
                for subresult in result:
                    fcnt+=1;
                    if fcnt >= 2:
                        fobj.write("\n%s"%subresult);
                        os.remove(subresult);
        print("Output is stored at %s"%log_path);
        fileProcTime=datetime.now().strftime('%Y-%m-%d_%H-%M-%S');
        return log_path,fileProcTime;
    else:
        print("No duplicate files found to delete!!");
        return False,False;

def findDups(path):

    flag=os.path.isabs(path);
    if flag == False:
        path=os.path.abspath(path);

    exists=os.path.exists(path);

    if exists:
        dupsfilesDic={};
        startTime=datetime.now().strftime('%Y-%m-%d_%H-%M-%S');
        totalFiles=0;
        dupFiles=0;
        for dirName, subDir, files in os.walk(path):
            for fname in files:
                totalFiles=len(files);
                fname=os.path.join(dirName,fname);
                file_hash= Checksum.hashfile(fname);
                if file_hash in dupsfilesDic:
                        dupsfilesDic[file_hash].append(fname);
                        dupFiles+=1;
                else:
                    dupsfilesDic[file_hash]=[fname];

        return dupsfilesDic,startTime,totalFiles,dupFiles;
    else:
        print("Invalid path");


def dupFileRemoval(dirName):
    arr,starTime,totalFiles,dupFiles= findDups(dirName);
    log_path,fileGenTime=DelDups(arr,dirName);
    if log_path and fileGenTime:
        connected = checkInternet.check_internet();
        if not connected:
            print("Not Connected to Internet.");
            print("Mail did not sent...");
        else:
            mailSender(log_path,str(sys.argv[3]),starTime,totalFiles,dupFiles,fileGenTime);
    else:
        print("Mail did not sent...")

def main():
      try:

        dirName=sys.argv[1];
        schedule.every(int(sys.argv[2])).seconds.do(dupFileRemoval,dirName);
        while True:
            schedule.run_pending();
            time.sleep(5);
      except Exception as E:
          print("Exception occured: ",E);


if __name__ == "__main__":
    main();
