from django.core.mail import EmailMessage


class Mail(EmailMessage):
    def __init__(self, subject=None, message=None, recipient=None):
        if not subject or not isinstance(subject, str):
            raise TypeError('subject must be of type "str"')

        if not message or not isinstance(message, str):
            raise TypeError('message must be of type str')

        if not recipient or not isinstance(recipient, str):
            raise TypeError('recipient email address must be of type str')

        super().__init__(subject=subject, body=message, to=[recipient])


    @staticmethod
    def send(subject, message, recipient):
        sent = False
        try:
            mail = Mail(subject, message, recipient)
            count = mail.send()
            if count != 1:
                raise Exception('There was an error in sending the email')

            sent = True
        except Exception as e:
            print(e)
        finally:
            return sent
