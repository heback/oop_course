class EmailNotification:
    def send_email(self,
                   recipient: str,
                   subject: str,
                   message: str) -> None:
        print(f"Sending email to {recipient} "
              f"with subject '{subject}' and message: {message}")


class SMSNotification:
    def send_sms(self,
                 phone_number: str,
                 subject: str,
                 message: str) -> None:
        print(f"Sending SMS to {phone_number} "
              f"with subject '{subject}' and message: {message}")


class MultiChannelNotification(EmailNotification, SMSNotification):
    def send_multimedia(self,
                        email_recipient: str,
                        phone_number: str,
                        subject: str,
                        email_message: str,
                        sms_message: str) -> None:
        self.send_email(email_recipient, subject, email_message)
        self.send_sms(phone_number, subject, sms_message)


# 사용 예제
notification = MultiChannelNotification()

notification.send_email(
    "user@example.com",
    "Hello",
    "This is an email message.")

notification.send_sms(
    "123-456-7890",
    "Hello",
    "This is an SMS message.")

notification.send_multimedia(
    "user@example.com",
    "123-456-7890",
    "Multimedia Alert",
    "This is an email alert",
    "This is an SMS alert"
)

