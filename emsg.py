from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


def semsg(body):
    email_sender = "manan.kateshiya111006@marwadiuniversity.ac.in"
    load_dotenv()
    email_password = os.getenv('EMAIL_KEY')
    
    email_rec = "manankateshiya@gmail.com"
    subject = "Sub"
    body = """ 
        Exact Time of Email: {} {}
    """.format(current_time, body)
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_rec
    em['subject'] = subject
    em.set_content(body)
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_rec, em.as_string())

# semsg(body)