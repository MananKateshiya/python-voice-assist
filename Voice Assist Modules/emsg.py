from email.message import EmailMessage
import ssl
import smtplib


def semsg():
    eemail_sender = "manan.kateshiya111006@marwadiuniversity.ac.in"
    email_password = "oravgbtobnhziapd"
    
    email_rec = "manankateshiya@gmail.com"
    subject = "Sub"
    body = """ 
        Test successfull!!!
    """
    
    em = EmailMessage()
    em['From'] = eemail_sender
    em['To'] = email_rec
    em['subject'] = subject
    em.set_content(body)
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(eemail_sender, email_password)
        smtp.sendmail(eemail_sender, email_rec, em.as_string())