import time
import smtplib as x
from multiprocessing import Process, Value, Lock

username = input("Email: ")
pword = input("Password: ")
number=1
server = x.SMTP_SSL('smtp.gmail.com', 465)
sender = 'Hey'
to = 'email'
subject = 'Maddie Said I should do this, blame here'
body = 'this is now super fast'
email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sender, to, subject, body)
print(server.ehlo())
def mail_send():
    global number, body
    while True:
        try:
            print(number)
            number+=1

            server.sendmail(sender,(to),str(email_text))
            time.sleep(1)
        except:
            server.connect()
            server.ehlo()
            server.login(username,pword)
if __name__ == '__main__':
    v= Value('i', 0)
    lock = Lock()

    y=Process(target=mail_send)
    z=Process(target=mail_send)
    y.start()
    z.start()
