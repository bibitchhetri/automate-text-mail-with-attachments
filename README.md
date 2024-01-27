# Personalized Email Automation

This project automates the process of sending personalized emails along with certificates to a list of recipients. It's was particularly designed for WordCamp Nepal events.

## Table of Contents

- [Folder Structure](#folder-structure)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Configuration](#configuration)
- [Customization](#customization)
- [License](#license)

## Directory Structure

```
./automate-text-mail-with-attachments
├── LICENSE
├── README.md
├── automatedTextMailWithAttachment.ipynb
├── requirements.txt
├── sendAutomatedTextMail.ipynb
├── sendMailAndCerts.py
├── src
│   ├── campList.csv
│   └── certs
│       ├── avibaral.png
│       ├── bibitkunwar.png
│       └── janamkunwar.png
├── textMailAutomation.py
```

## Prerequisites

- Python installed (version 3.x recommended)
- Jupyter Notebook for running the provided .ipynb files
- Gmail account for sending emails
- Certificates in the `certs` folder named following the format: `Name.png`

## Usage

1. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the `sendMailAndCerts.py` script:

   ```bash
   python3 sendMailAndCerts.py
   ```

   This script will read the recipient list from `campList.csv`, personalize the email content, attach certificates from the `certs` folder, and send emails using your Gmail account.

## Configuration

Update the following configurations in the `sendMailAndCerts.py` script:

- `sender_email`: Your Gmail email address.
- `sender_password`: Your Gmail app password (generate one in your Google Account settings).
- `smtp_server`: SMTP server for Gmail (default: 'smtp.gmail.com').
- `smtp_port`: SMTP port for Gmail (default: 587).

## Customization

Feel free to customize the email content and structure in the `sendMailAndCerts.py` script. You can also modify the certificate filenames and formats according to your needs.

## License

This project is licensed under the [MIT License](LICENSE).
