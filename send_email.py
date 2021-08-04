import smtplib
import sys
from email.message import EmailMessage
from string import Template
from pathlib import Path


def main():
    html = Template(Path('index.html').read_text())
    receiver_email, receiver_name, sender_email, sender_password = sys.argv[1:]

    email = EmailMessage()
    email['from'] = 'Silly Python Bot'
    email['to'] = receiver_email
    email['subject'] = 'You won 1 million dollars!'

    email.set_content(html.substitute(name=receiver_name), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.send_message(email)


if __name__ == '__main__':
    main()
