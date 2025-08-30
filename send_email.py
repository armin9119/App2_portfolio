import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465

username = 'armincook7@gmail.com'
password = 'epfl zcaz lrwx fyra'

receiver = 'armincook7@gmail.com'

context = ssl.create_default_context()

message = """\
Subject: Hi
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)


# Add navigation menu and
# Contact Us page and send email