import smtplib, ssl
from email.mime.text import MIMEText


class EmailSender:

    def __init__(self, receivers=["senster2000@gmail.com", "alexandregoode@gmail.com"]):
        self.sender = "L3W.G4.SAD@gmail.com"
        self.sender_password = "SYSC3010"
        self.receivers = receivers

    def die(self):
        s.quit()

    def create_and_send_email(self, person, reason):
        self.s = smtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465)
        self.s.login(user = self.sender, password = "SYSC3010")
        body_of_email = "There is someone at the door that failed their screening.\n User: " + person + "\nReason: " + reason

        msg = MIMEText(body_of_email, "html")
        msg["Subject"] = "Screening Failed - " + person + " " + reason
        msg["From"] = self.sender
        msg["To"] = ",".join(self.receivers)

        self.s.sendmail(self.sender, self.receivers, msg.as_string())
