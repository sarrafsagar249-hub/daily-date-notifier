import os
import smtplib
import pytz
import nepali_datetime

from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# India Date
india = datetime.now(pytz.timezone("Asia/Kolkata"))

india_date = india.strftime("%A, %d %B %Y")
day = india.strftime("%A")

# Nepal Date
nepal = nepali_datetime.date.today()

nepal_date = nepal.strftime("%K %d, %N %Y")

# Email
sender = os.environ["EMAIL_ADDRESS"]
password = os.environ["EMAIL_PASSWORD"]
receivers = os.environ["RECEIVER_EMAIL"].split(",")

subject = "🌅 Today's India & Nepal Date"

body = f"""
Good Morning!

🇳🇵 Nepal (BS)

{nepal_date}

🇮🇳 India (AD)

{india_date}

📅 Day

{day}

Have a wonderful day!
"""

message = MIMEMultipart()
message["From"] = sender
message["To"] = ", ".join(receivers)
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender, password)

server.sendmail(
    sender,
    receivers,
    message.as_string()
)

server.quit()

print("Email sent successfully.")
