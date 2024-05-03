import email, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from providers import PROVIDERS

def send_mms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "sent using etext",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465
):
    
    sender_email, email_password = sender_credentials
    receiver_email = f"{number}@{PROVIDERS.get(provider).get('mms')}"  # Use MMS gateway
    
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    # Add body to email
    msg.attach(MIMEText(message, 'plain'))
    
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

def main():
    number = "7342942472"
    provider = "Xfinity Mobile"
    subject = "Test MMS"
    sender_credentials = ("yasin.hasan4242@gmail.com", "lkgfhljffdhajdby") #MOVE TO .END FILE

    send_mms_via_email(number, "TEST TEST", provider, sender_credentials, "Test Message Test Message")

if __name__ == "__main__":
    main()


