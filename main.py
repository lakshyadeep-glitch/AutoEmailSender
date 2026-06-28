import smtplib
from email.message import EmailMessage

def send_email(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = 'your-email@gmail.com'
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('your-email@gmail.com', 'your-app-password')
            smtp.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

# Example usage
send_email(
    subject="Hello from Python!",
    body="This is an automated email.",
    to_email="friend@example.com"
)
