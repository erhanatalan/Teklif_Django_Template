from .veri import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from django.conf import settings

def sendemail(sender_email, sender_password, recipient_email, subject, message1):

    
    # Create a multipart message object
    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Create both plain text and HTML versions of the email
    text = 'This is a plain text email.'
    html = f'<html><body><p>{message1}</p></body></html>'

    # Attach the plain text and HTML versions to the email
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # word_dizini = 'C:/Users/yenic/Desktop/Teklif_Django_Template/otomatik/word/'
    pdf_dizini = os.path.join(settings.BASE_DIR, 'otomatik/pdf')
    # pdf_dizini = 'C:/Users/yenic/Desktop/Teklif_Django_Template/otomatik/pdf/'

    with open(f'{pdf_dizini}/{dosya1}.pdf', 'rb') as file:
        pdf = MIMEApplication(file.read())
        pdf.add_header('Content-Disposition', 'attachment', filename=f'{dosya1}.pdf')
        msg.attach(pdf)
    with open(f'{pdf_dizini}/{dosya2}.pdf', 'rb') as file1:
        pdf1 = MIMEApplication(file1.read())
        pdf1.add_header('Content-Disposition', 'attachment', filename=f'{dosya2}.pdf')
        msg.attach(pdf1)

    msg.attach(part1)
    msg.attach(part2)

    # SMTP server settings for Outlook
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587

    try:
        # Create a secure SSL/TLS connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to your Outlook email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print("Error sending email:", str(e))

    finally:
        # Close the connection to the SMTP server
        server.quit()

