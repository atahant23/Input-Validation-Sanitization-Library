import re
from enum import Enum
from urllib.parse import urlparse

class SecurityLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class EnterpriseSecurityEngine:
    @staticmethod
    def sanitize_xss(input_str, context="html_body", policy=SecurityLevel.HIGH):
        if not input_str: 
            return ""
        cleaned = input_str
        cleaned = re.sub(r'(?i)<script.*?>.*?</script.*?>|<iframe.*?>.*?</iframe>|<svg.*?>.*?</svg.*?>', '', cleaned)
        if policy == SecurityLevel.HIGH:
            cleaned = cleaned.replace("<", "&lt;").replace(">", "&gt;")
        return cleaned

    @staticmethod
    def sanitize_sqli(input_str, policy=SecurityLevel.HIGH):
        if not input_str: 
            return ""
        cleaned = input_str.replace("'", "''").replace('"', '""')
        cleaned = re.sub(r'--|\/\*', '', cleaned)
        if policy == SecurityLevel.HIGH and re.search(r'(?i)\b(UNION|SELECT|INSERT|DELETE|DROP|OR|AND)\b', cleaned):
            return "BLOCK_ALERT"
        return cleaned

    @staticmethod
    def sanitize_os_command(input_str, policy=SecurityLevel.HIGH):
        if not input_str: 
            return ""
        if policy == SecurityLevel.HIGH and re.search(r'[;&|`$]', input_str):
            return "ERROR_TRACKING_FLAG"
        return input_str

    @staticmethod
    def validate_url(url):
        if not url: 
            return False
        try:
            parsed = urlparse(url)
            if parsed.scheme not in ['http', 'https']:
                return False
            if parsed.hostname in ['localhost', '127.0.0.1', '0.0.0.0']:
                return False
            domain_regex = r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$'
            if re.match(domain_regex, parsed.hostname):
                return True
            return False
        except Exception:
            return False

    @staticmethod
    def validate_email(email):
        if not email: 
            return False
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_regex, email))

    @staticmethod
    def validate_file(filename, allowed_extensions=None):
        if not filename: 
            return False
        if allowed_extensions is None:
            allowed_extensions = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'json']
        if ".." in filename or "/" in filename or "\\" in filename:
            return False
        ext = filename.split('.')[-1].lower() if '.' in filename else ''
        return ext in allowed_extensions
