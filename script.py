import smtplib
import sys
from email.message import EmailMessage


def main():
    receiver_email, sender_email, sender_password = sys.argv[1:]

    email = EmailMessage()
    email['from'] = 'Some Python Bot'
    email['to'] = receiver_email
    email['subject'] = 'You won 1 million dollars!'

    email.set_content('This is the content!')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.send_message(email)


if __name__ == '__main__':
    main()
