import resend
from app.utils.load_env import env
from app.templates.email.verification_email import generate_verification_email

class Email:
    def __init__(self, resend_api_key: str):
        self.api_key = resend_api_key
        resend.api_key = self.api_key

    def send_verification_email(self, email: str, verification_code: str):
        try:
            resend.Emails.send({
                "from": "Acme <onboarding@resend.dev>",
                "to": email,
                "subject": "Verify your email",
                "html": generate_verification_email(verification_code, email)
            })
        except Exception as e:
            raise e
    
    def send_email(self, params: resend.Emails.SendParams):
        try:
            resend.Emails.send(params)
        except Exception as e:
            raise e
        
email = Email(env.get_env_variable("RESEND_API_KEY"))