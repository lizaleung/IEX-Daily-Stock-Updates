import smtplib
import datetime
import os
from email.mime.multipart import MIMEMultipart

class Gmail:
    def __init__(self):
        return

    def send_email(self, body):
        try:
            gmail_user = os.environ.get('GMAIL_EMAIL')
            gmail_password = os.environ.get('GMAIL_PW')

            msg = MIMEMultipart('alternative')
            msg.attach(body)
            msg['From'] = ''
            msg['To'] = ''
            now = datetime.datetime.now()
            msg['Subject'] = str(now.month) + '-' + str(now.day) + '-' + str(now.year) + ' Stock Insights'

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.close()

        except Exception as e:
            print (str(e))