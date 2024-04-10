import os
import datetime
from ftplib import FTP 

source_directory="/home"
now = datetime.datetime.now()
remote_directory=now.strftime("%y-%m-%d")


hostname='your server ip'
username='ftp username'
password='ftp password'


def upload(ftp, local_directory, remote_directory):
    ftp.mkd(remote_directory)
    ftp.cwd(remote_directory)
    for item in os.listdir(local_directory):
        local_path = os.path.join(local_directory, item)
        if os.path.isfile(local_path):
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {item}', f)
        elif os.path.isdir(local_path):
            upload(ftp, local_path, item)
    ftp.cwd('..')



ftp=FTP(hostname,username,password)


print("connected!")
upload(ftp,source_directory,remote_directory)

ftp.quit()
print("disconnectd!")