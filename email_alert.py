import smtplib
import datetime
import threading

alert_sent = False
def send_alert(timestamp):
    global alert_sent
    if alert_sent:
        return
    alert_sent=True
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
        server.starttls()
        server.login("moulyar05@gmail.com", "kufm civh jusb qtbu")
        message=f"Accident detected at {timestamp}, make arrangements"
        server.sendmail("moulyar05@gmail.com", "police@gmail.com", message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e :
        print("Email failed:", e)