# # smtp_test.py
# import smtplib, os
# from email.message import EmailMessage

# SMTP_HOST = os.getenv("SMTP_HOST") or "smtp.gmail.com"
# SMTP_PORT = int(os.getenv("SMTP_PORT") or 587)
# SMTP_USER = os.getenv("SMTP_USER")
# SMTP_PASS = os.getenv("SMTP_PASS")
# TO = SMTP_USER  # send to yourself for test

# msg = EmailMessage()
# msg["From"] = SMTP_USER
# msg["To"] = TO
# msg["Subject"] = "TaskPilot SMTP test"
# msg.set_content("This is a test email from TaskPilot. If you see this, SMTP works!")

# try:
#     with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20) as s:
#         s.ehlo()
#         s.starttls()
#         s.ehlo()
#         s.login(SMTP_USER, SMTP_PASS)
#         s.send_message(msg)
#     print("Email sent successfully")
# except Exception as e:
#     print("Error sending email:", e)


import smtplib
from email.message import EmailMessage

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "sonamsultana95@gmail.com"
SMTP_PASS = "klorwlckfnfcydeq"  # paste exactly, no spaces

msg = EmailMessage()
msg["From"] = SMTP_USER
msg["To"] = SMTP_USER
msg["Subject"] = "SMTP direct test"
msg.set_content("If you see this, SMTP login worked!")

try:
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
    print("✅ Email sent successfully")
except Exception as e:
    print("❌ Error:", e)
