import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content

API_KEY = 'SENDGRID_API_KEY'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, name):
    from_email = Email("manika.kapoor90@gmail.com")
    to_email = Email(email)
    subject = SUBJECT
    content = Content("text/plain", "Hi " + name)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')

