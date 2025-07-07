import psutil
import logging
import smtplib
from email.message import EmailMessage
import datetime

# CONFIG
DRIVE = "C:\\"
THRESHOLD_PERCENT = 10
LOG_FILE = "disk_monitor.log"
EMAIL_TO = "it-team@it.com.au"
EMAIL_FROM = "anupshrestha036@buisness.com.au"
EMAIL_PASSWORD = "123456"

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def check_disk():
    usage = psutil.disk_usage(DRIVE)
    percent_free = 100 - usage.percent

    if percent_free < THRESHOLD_PERCENT:
        message = f"🚨 WARNING: Only {percent_free:.2f}% disk space left on {DRIVE}"
        logging.warning(message)
        send_email_alert(message)
    else:
        logging.info(f"✅ Disk check OK. Free space: {percent_free:.2f}%")


def send_email_alert(body):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = f"[Disk Alert] Low Disk Space on {DRIVE}"
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_FROM, EMAIL_PASSWORD)
            smtp.send_message(msg)

        logging.info("📧 Alert email sent successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to send email: {e}")


if __name__ == "__main__":
    check_disk()

