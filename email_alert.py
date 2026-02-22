# Handles email alerts when fall is detected
# Sends only once per session using alert_sent flag

import smtplib
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Flag to prevent multiple emails per session
alert_sent = False
def send_alert(timestamp):
    global alert_sent
    if alert_sent:
        return
    alert_sent=True
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
        server.starttls()
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")
        server.login(email, password)
        message=f"Accident detected at {timestamp}, make arrangements"
        server.sendmail("moulyar05@gmail.com", "police@gmail.com", message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e :
        print("Email failed:", e)