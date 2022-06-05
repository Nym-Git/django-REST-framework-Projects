import smtplib
from email.message import EmailMessage


def send_mail(to_address,subject,body):
    EMAIL_ADDRESS = 'nym673@gmail.com'
    EMAIL_PASSWORD = 'z00nym@BCALOL'

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['from'] = EMAIL_ADDRESS
    msg['TO'] = to_address                                     
    msg.set_content(body)
    #msg.add_alternative(body, subtype='html')
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    
    
    