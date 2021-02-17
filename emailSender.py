
import os
import smtplib

EMAIL_ADDRESS = 'YOUR EMAIL'
EMAIL_PASSWORD = 'YOUR PASSWORD'


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    #connects to server
    smtp.ehlo()
    #encrpyts the connection
    smtp.starttls()
    #reidentifies that its a encrypted connection
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6pm this saturday'

    msg = f'Subject: {subject}\n\n{body}'

    #email sender, reciever, then the message
    smtp.sendmail(EMAIL_ADDRESS, 'jacobhoskins779@icloud.com', msg)

