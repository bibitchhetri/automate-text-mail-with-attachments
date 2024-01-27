import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'your_mail@gmail.com'
sender_password = 'gmail_pass_key'
subject = 'provide subject here'

message_template = """
Dear {recipient_name},

I hope this message finds you well. I'm reaching out to introduce you to our latest demo, {demo_name}. 
With features like {feature_1} and {feature_2}, it's designed to {brief_description}. I'd love to offer
you a quick, personalized demo at your convenience. Are you available for a brief call this week?

Best regards,
{your_full_name}
{your_company}
"""

csv_file_path = 'src/campList.csv'

smtp_server = 'smtp.gmail.com'
smtp_port = 587

def read_recipients_from_csv(csv_file_path):
    recipients = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            recipients.append(row)
    return recipients

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, sender_password)

# Read recipients from CSV file
recipients = read_recipients_from_csv(csv_file_path)

# Send emails
for recipient in recipients:
    personalized_message = message_template.format(
        recipient_name=recipient['Name'],
        # replace your info below
        demo_name='WordCamp Nepal',
        feature_1='Organizers',
        feature_2='Volunteers',
        brief_description='Organizers & Volunteers',
        your_full_name='WordPress Pokhara',
        your_company='WordCamp Nepal'
    )

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient['Email']
    msg['Subject'] = subject
    msg.attach(MIMEText(personalized_message, 'plain'))

    try:
        # Send the email
        server.sendmail(sender_email, recipient['Email'], msg.as_string())
        print(f"Email sent successfully to {recipient['Email']}")
    except smtplib.SMTPException as e:
        print(f"Failed to send email to {recipient['Email']}. Error: {e}")

# Quit the server after sending all emails
server.quit()