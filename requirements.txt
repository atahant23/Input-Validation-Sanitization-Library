mkdir -p src && cat << 'EOF' > src/sanitizer.py
import re
import html
import urllib.parse

class AdvancedSecuritySanitizer:
    @staticmethod
    def sanitize_xss(payload: str) -> str:
        if not isinstance(payload, str): return ""
        decoded = urllib.parse.unquote(payload)
        decoded = html.unescape(decoded)
        previous = ""
        while previous != decoded:
            previous = decoded
            decoded = re.sub(r'<(script|iframe|object|embed|applet|meta|link|style)[^>]*>.*?</\1>', '', decoded, flags=re.IGNORECASE|re.DOTALL)
            decoded = re.sub(r'<(script|iframe|object|embed|applet|meta|link|style)[^>]*>', '', decoded, flags=re.IGNORECASE)
        decoded = re.sub(r'\son\w+\s*=', ' removed_event=', decoded, flags=re.IGNORECASE)
        decoded = re.sub(r'javascript\s*:', 'removed_proto:', decoded, flags=re.IGNORECASE)
        decoded = re.sub(r'data\s*:', 'removed_proto:', decoded, flags=re.IGNORECASE)
        return html.escape(decoded)

    @staticmethod
    def sanitize_sqli(payload: str) -> str:
        if not isinstance(payload, str): return ""
        decoded = urllib.parse.unquote(payload)
        decoded = html.unescape(decoded)
        dangerous_chars = ["'", '"', ";", "--", "/*", "*/", "#"]
        for char in dangerous_chars:
            decoded = decoded.replace(char, "")
        sql_patterns = [
            r"\b(UNION|SELECT|INSERT|UPDATE|DELETE|DROP|ALTER|GRANT|REVOKE)\b",
            r"\b(OR|AND)\s+\d+\s*=\s*\d+",
            r"\b(OR|AND)\s+['\"].+['\"]\s*=\s*['\"].+['\"]"
        ]
        for pattern in sql_patterns:
            decoded = re.sub(pattern, "[SQLI_BLOCKED]", decoded, flags=re.IGNORECASE)
        return decoded.strip()
EOF
