import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # Email content
    from_email = "your_mail_id"
    to_email = "recepent_mail_id"
    subject = "Daily Report"
    body = "This is the daily report for your business."

    # Email server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your_mail_id"
    smtp_password = "your_password"

    # Create message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send email
    server.sendmail(from_email, to_email, msg.as_string())

    # Quit SMTP server
    server.quit()

    print("Email sent successfully.")

# Send email immediately
send_email()
