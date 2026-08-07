import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "syedimad305@gmail.com"
    password = "vgzompbfhuhdybiq"

    receiver = "closaif@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        
if __name__ == "__main__":
    send_email("For myself")
