import os
import smtplib
import csv
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

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
certs_folder = 'src/certs'

smtp_server = 'smtp.gmail.com'
smtp_port = 587

def read_recipients_from_csv(csv_file_path):
    recipients = []
    with open(csv_file_path, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            recipients.append(row)
    return recipients

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, sender_password)

recipients = read_recipients_from_csv(csv_file_path)

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

    certificate_filename = recipient['Name'].replace(' ', '').lower() + '.png'
    certificate_filename = certificate_filename.replace('\ufeff', '')
    certificate_path = os.path.join(certs_folder, certificate_filename)

    print(f"Processing {recipient['Name']}, Certificate: {certificate_filename}")

    if os.path.exists(certificate_path):
        print(f"Certificate found for {recipient['Name']}.")
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient['Email']
        msg['Subject'] = subject
        msg.attach(MIMEText(personalized_message, 'plain'))

        with open(certificate_path, 'rb') as cert_file:
            cert_attachment = MIMEApplication(cert_file.read(), Name=os.path.basename(certificate_path))
            cert_attachment['Content-Disposition'] = f'attachment; filename={os.path.basename(certificate_path)}'
            msg.attach(cert_attachment)

        try:
            server.sendmail(sender_email, recipient['Email'], msg.as_string())
            print(f"Email sent successfully to {recipient['Email']} with certificate.")
        except smtplib.SMTPException as e:
            print(f"Failed to send email to {recipient['Email']}. Error: {e}")
    else:
        print(f"Certificate not found for {recipient['Name']}. Skipping email.")

    time.sleep(2)

server.quit()
print('Emails sent successfully.')
