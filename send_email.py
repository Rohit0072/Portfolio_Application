import smtplib
import ssl


def send_email(message):

    host = "smtp.gmail.com"
    port = 465
    username = "rs3274357@gmail.com"
    password = "mwlfktxtmbykzzem"

    receiver = "rs3274357@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

