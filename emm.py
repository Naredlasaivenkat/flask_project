from email.message import EmailMessage
import ssl
import smtplib


def emai(recv,name):
    email_send = "microproject234@gmail.com"
    email_pass = "aucdvwtvfprjtwzg"
    subject = "Explore-X"
    body = "Thank you {} for login in our website ".format(name)
    em = EmailMessage()
    em['From'] = email_send
    em['To'] = recv
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_send, email_pass)
        smtp.send_message(em)


