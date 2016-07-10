import subprocess
import smtplib
import socket

from email.mime.text import MIMEText
import datetime
from TempHumidity import *

###
# Change to your settings
###
pi_name = 'your-pi'
to = 'somebody@somewhere.com'

## Feel free to reuse, but please don't abuse the techem student relay
mail_user = 'xxx@techemstudios.com'
mail_password = 'pword'
smtp_server = 'smtp.somwhere.net'
smtp_port = 3535 # Use 587 for gmail

def deliver ( message, subject = 'RPi output' ):
    smtpserver = smtplib.SMTP(smtp_server,smtp_port) # Use 587 for gmail
    smtpserver.ehlo()
    #smtpserver.starttls() # Uncomment this line for gmail
    smtpserver.ehlo
    smtpserver.login(mail_user, mail_password)
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = '(%s)%s' % (pi_name,mail_user)
    msg['To'] = to
    smtpserver.sendmail(mail_user, [to], msg.as_string())
    smtpserver.quit()

deliver('The current temp is %0.2f C, %0.2f F, with a humidty of %0.2f%%' % (read_temp_humidity()))
