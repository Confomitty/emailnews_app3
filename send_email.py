import smtplib, ssl
import os

# just try to understand the below code that is all

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    userkanaam = os.getenv("username")
    passkaword = os.getenv("password")

    receivaar = os.getenv("receiver")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(userkanaam, passkaword)
        server.sendmail(userkanaam, receivaar, message)
        
if __name__ == "__main__":
    send_email("This email was sent to you through Python code , rather than manual sending. Just a test")
