import smtplib
from email.mime.text import MIMEText
import user_config  # (you’ll store these values here safely)

def send_email_via_brevo(to_email, subject, body):
    from_email = user_config.brevo_user     # your SMTP login user
    password   = user_config.brevo_smtp_key  # your SMTP key (password)

    try:
        msg = MIMEText(body, "plain")
        msg["Subject"] = subject
        msg["From"]    = from_email
        msg["To"]      = to_email

        server = smtplib.SMTP("smtp-relay.brevo.com", 587, timeout=30)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        return True, "Email sent successfully!"
    except Exception as e:
        return False, f"Error sending email via Brevo: {e}"
