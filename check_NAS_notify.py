import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time

# Configuration
nas_ip = '192.168.1.1'  # Replace with your NAS IP address
check_interval = 60  # Check every 60 seconds
email_sender = 'your_email@example.com'
email_receiver = 'recipient@example.com'
email_subject = 'NAS Offline Alert'
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_email@example.com'
smtp_password = 'your_password'

def is_nas_online(ip):
    """Check if NAS is online by pinging it."""
    try:
        output = subprocess.check_output(['ping', '-c', '1', ip], stderr=subprocess.STDOUT, text=True)
        return '1 packets transmitted, 1 received' in output
    except subprocess.CalledProcessError:
        return False

def send_email(subject, body):
    """Send an email notification."""
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(email_sender, email_receiver, msg.as_string())

def main():
    while True:
        if not is_nas_online(nas_ip):
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_message = f"NAS is offline. Timestamp: {timestamp}"
            print(log_message)
            with open('nas_offline_log.txt', 'a') as log_file:
                log_file.write(log_message + '\n')

            email_body = f"The NAS at {nas_ip} was detected as offline.\n\nTimestamp: {timestamp}"
            send_email(email_subject, email_body)
        
        time.sleep(check_interval)

if __name__ == "__main__":
    main()