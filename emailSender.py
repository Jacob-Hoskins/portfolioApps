
import os
import smtplib
from tkinter import *
'''
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

'''

root = Tk()
root.geometry('350x400')

class MainGui:

    def __init__(self, master):
        sendToLabel = Label(master, text="Send to")
        sendToLabel.pack()
        self.sendToEntry = Entry(master)
        self.sendToEntry.pack()
        usernameLabel = Label(master, text="Email")
        usernameLabel.pack()
        self.usernameEntry = Entry(master)
        self.usernameEntry.pack()
        passwordLabel = Label(master, text="Password")
        passwordLabel.pack()
        self.passwordEntry = Entry(master)
        self.passwordEntry.pack()
        subjectLabel = Label(master, text="Subject")
        subjectLabel.pack()
        self.subjectEntry = Entry(master)
        self.subjectEntry.pack()
        bodyLabel = Label(master, text="Body")
        bodyLabel.pack()
        self.bodyEntry = Entry()
        self.bodyEntry.pack()
        sendButton = Button(master, text="send", command=self.sendEmail)
        sendButton.pack()
        self.port = 587

    def sendEmail(self):
        reciver = self.sendToEntry.get()
        email = self.usernameEntry.get()
        password = self.passwordEntry.get()
        subject = self.subjectEntry.get()
        body = self.bodyEntry.get()


        with smtplib.SMTP('smtp.gmail.com', self.port) as smtp:
            # connects to server
            smtp.ehlo()
            # encrpyts the connection
            smtp.starttls()
            # reidentifies that its a encrypted connection
            smtp.ehlo()

            smtp.login(email, password)

            msg = f'Subject: {subject}\n\n{body}'

            # email sender, reciever, then the message
            smtp.sendmail(email, reciver, msg)

            print("Email Sent")


if __name__ == '__main__':
    app = MainGui(root)
    app

root.mainloop()