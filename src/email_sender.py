import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .config import Config
from .logger import log


def send_email(message: str, config: Config) -> bool:
    for attempt in range(config.max_retries):
        try:
            log.info(f"Sending email (attempt {attempt + 1}/{config.max_retries})...")

            msg = MIMEMultipart("alternative")
            msg["Subject"] = "AI Research Daily Digest"
            msg["From"] = config.sender_email
            msg["To"] = config.recipient_email
            msg.attach(MIMEText(message, "plain"))

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=config.request_timeout) as server:
                server.login(config.sender_email, config.sender_app_password)
                server.sendmail(config.sender_email, config.recipient_email, msg.as_string())

            log.info("Email sent successfully.")
            return True

        except smtplib.SMTPAuthenticationError:
            log.error("Gmail authentication failed. Check sender_email and app password.")
            return False

        except (smtplib.SMTPException, OSError) as e:
            log.warning(f"Send failed: {e}")
            if attempt == config.max_retries - 1:
                return False
            time.sleep(config.retry_delay * (attempt + 1))

    return False
