import smtplib, ssl
import json

# Set up SMTP server and port
smtp_server = "smtp.gmail.com"
port = 587

# Read credentials from JSON file
def read_cred():
    with open("creds.json", "r") as cred_file:
        creds = json.load(cred_file)
    return creds

# Set up credentials
creds = read_cred()
sender = creds["sender"]
sender_name = creds["sender_name"]
sender_password = creds["sender_password"]
recipient = creds["recipient"]

# Set up email content
message = """From: {} <{}>
To: <{}>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML email test

This is an email message to be sent in HTML format. <br>

<b>This is HTML message.</b>
<h1>This is headline.</h1>
Hello there!
""".format(sender_name, sender, recipient)

# Enact SMTP protocols
ssl_context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context = ssl_context)
    server.login(sender, sender_password)
    server.sendmail(sender, recipient, message)