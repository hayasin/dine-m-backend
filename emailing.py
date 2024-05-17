import os
import smtplib
from dotenv import load_dotenv
load_dotenv()

def send_email(subject, message, email_receiver):
    email = os.getenv("GMAIL")
    email_password = os.getenv("GMAIL_PASSWORD")

    subject = subject.strip()
    message = message.strip()
    email_receiver = email_receiver.replace('\n', '').strip()

    text = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, email_password)
    server.sendmail(email, email_receiver, text)
    server.quit()

