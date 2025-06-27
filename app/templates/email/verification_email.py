from app.core.config import PRIVACY_POLICY_URL, TERMS_OF_SERVICE_URL, UNSUBSCRIBE_URL, PROJECT_NAME
from datetime import datetime
def generate_verification_email(verification_code: str, email: str):
    """
    Generate a professional HTML email template with verification code.
    Adaptive to both dark and light mode with inline CSS.
    
    Args:
        verification_code (str): The verification code to include in the email
        
    Returns:
        str: Complete HTML email template with inline CSS
    """
    
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="color-scheme" content="light dark">
    <meta name="supported-color-schemes" content="light dark">
    <title>Verify Your Email</title>
    <style>
        @media (prefers-color-scheme: dark) {{
            .email-container {{ background-color: #000000 !important; color: #ffffff !important; }}
            .email-content {{ background-color: #111111 !important; border-color: #333333 !important; }}
            .verification-code {{ background-color: #1a1a1a !important; border-color: #333333 !important; color: #ffffff !important; }}
            .footer-text {{ color: #888888 !important; }}
            .link {{ color: #0070f3 !important; }}
        }}
        
        @media (prefers-color-scheme: light) {{
            .email-container {{ background-color: #ffffff !important; color: #000000 !important; }}
            .email-content {{ background-color: #ffffff !important; border-color: #e1e1e1 !important; }}
            .verification-code {{ background-color: #f8f9fa !important; border-color: #e1e1e1 !important; color: #000000 !important; }}
            .footer-text {{ color: #666666 !important; }}
            .link {{ color: #0070f3 !important; }}
        }}
    </style>
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif; line-height: 1.6; background-color: #f5f5f5;">
    
    <div class="email-container" style="background-color: #f5f5f5; padding: 40px 20px; min-height: 100vh;">
        
        <!-- Header -->
        <div style="text-align: center; margin-bottom: 40px;">
            <div style="display: inline-block; padding: 12px 24px; background-color: #000000; border-radius: 50px; margin-bottom: 20px;">
                <span style="color: #ffffff; font-weight: 600; font-size: 16px; letter-spacing: 0.5px;">VERIFY</span>
            </div>
        </div>
        
        <!-- Main Content -->
        <div class="email-content" style="max-width: 500px; margin: 0 auto; background-color: #ffffff; border-radius: 12px; border: 1px solid #e1e1e1; padding: 40px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);">
            
            <!-- Title -->
            <h1 style="margin: 0 0 24px 0; font-size: 24px; font-weight: 600; color: inherit; text-align: center;">
                Verify your email address
            </h1>
            
            <!-- Description -->
            <p style="margin: 0 0 32px 0; font-size: 16px; color: inherit; text-align: center; opacity: 0.8;">
                Please use the verification code below to complete your email verification process.
            </p>
            
            <!-- Verification Code -->
            <div class="verification-code" style="background-color: #f8f9fa; border: 1px solid #e1e1e1; border-radius: 8px; padding: 24px; margin: 32px 0; text-align: center;">
                <div style="font-size: 14px; font-weight: 500; margin-bottom: 8px; opacity: 0.7; text-transform: uppercase; letter-spacing: 0.5px;">
                    Verification Code
                </div>
                <div style="font-size: 32px; font-weight: 700; font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace; letter-spacing: 4px; color: inherit;">
                    {verification_code}
                </div>
            </div>
            
            <!-- Instructions -->
            <div style="background-color: rgba(0, 112, 243, 0.05); border-left: 3px solid #0070f3; padding: 16px 20px; margin: 32px 0; border-radius: 0 6px 6px 0;">
                <p style="margin: 0; font-size: 14px; color: inherit; opacity: 0.8;">
                    <strong>Important:</strong> This code will expire in 10 minutes. If you didn't request this verification, please ignore this email.
                </p>
            </div>
            
            <!-- Alternative Action -->
            <div style="text-align: center; margin-top: 32px;">
                <p style="margin: 0 0 16px 0; font-size: 14px; color: inherit; opacity: 0.7;">
                    Having trouble? You can also verify by clicking the button below:
                </p>
                <a href="#" class="link" style="display: inline-block; background-color: #0070f3; color: #ffffff; text-decoration: none; padding: 12px 24px; border-radius: 6px; font-weight: 500; font-size: 14px; transition: background-color 0.2s;">
                    Verify Email Address
                </a>
            </div>
        </div>
        
        <!-- Footer -->
        <div style="max-width: 500px; margin: 40px auto 0; text-align: center;">
            <p class="footer-text" style="margin: 0 0 8px 0; font-size: 12px; color: #666666;">
                This email was sent to you because you requested email verification.
            </p>
            <p class="footer-text" style="margin: 0; font-size: 12px; color: #666666;">
                If you have any questions, please contact our support team.
            </p>
            
            <!-- Social Links -->
            <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid #e1e1e1;">
                <p class="footer-text" style="margin: 0 0 12px 0; font-size: 12px; color: #666666;">
                    © {datetime.now().year} {PROJECT_NAME}. All rights reserved.
                </p>
                <div style="display: inline-block;">
                    <a href="{PRIVACY_POLICY_URL}" class="link" style="color: #0070f3; text-decoration: none; font-size: 12px; margin: 0 8px;">Privacy Policy</a>
                    <span style="color: #e1e1e1;">|</span>
                    <a href="{TERMS_OF_SERVICE_URL}" class="link" style="color: #0070f3; text-decoration: none; font-size: 12px; margin: 0 8px;">Terms of Service</a>
                    <span style="color: #e1e1e1;">|</span>
                    <a href="{UNSUBSCRIBE_URL+"?/email={email}"}" class="link" style="color: #0070f3; text-decoration: none; font-size: 12px; margin: 0 8px;">Unsubscribe</a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
    """
    
    return html_template.strip()