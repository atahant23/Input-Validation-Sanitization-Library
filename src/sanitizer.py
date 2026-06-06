import re
import html
import urllib.parse
import json
import os
from datetime import datetime

class SecurityLevel:
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    PARANOID = 4

class EnterpriseSecurityEngine:
    
    @staticmethod
    def log_security_event(module: str, payload: str, level: int, action: str):
        event = {
            "timestamp": datetime.now().isoformat(),
            "security_module": module,
            "severity_level": "CRITICAL" if level >= 3 else "WARNING",
            "detected_payload": payload,
            "mitigation_action": action
        }
        try:
            os.makedirs("reports", exist_ok=True)
            with open("reports/security_alerts.json", "a") as f:
                f.write(json.dumps(event) + "\n")
        except:
            pass
        return event

    @staticmethod
    def sanitize_xss(payload: str, context: str = "html_body", policy: int = SecurityLevel.HIGH) -> str:
        if not isinstance(payload, str):
            return ""
        
        decoded = urllib.parse.unquote(payload)
        decoded = html.unescape(decoded)
        
        if policy == SecurityLevel.LOW:
            return html.escape(decoded)

        previous = ""
        while previous != decoded:
            previous = decoded
            decoded = re.sub(r'<(script|iframe|object|embed|applet|meta|link|style|svg|body|html|audio|video)[^>]*>.*?</\1>', '', decoded, flags=re.IGNORECASE|re.DOTALL)
            decoded = re.sub(r'<(script|iframe|object|embed|applet|meta|link|style|svg|body|html|audio|video)[^>]*>', '', decoded, flags=re.IGNORECASE)

        if policy >= SecurityLevel.MEDIUM:
            decoded = re.sub(r'\son\w+\s*=', ' blocked_event=', decoded, flags=re.IGNORECASE)
            decoded = re.sub(r'javascript\s*:', 'blocked_proto:', decoded, flags=re.IGNORECASE)
            decoded = re.sub(r'data\s*:', 'blocked_proto:', decoded, flags=re.IGNORECASE)

        if policy >= SecurityLevel.HIGH:
            if context == "html_attr":
                decoded = decoded.replace('"', '&quot;').replace("'", '&#x27;').replace('`', '&#x60;')
            elif context == "javascript":
                decoded = decoded.replace('\\', '\\\\').replace("'", "\\'").replace('"', '\\"')

        if policy == SecurityLevel.PARANOID:
            EnterpriseSecurityEngine.log_security_event("XSS", payload, policy, "PARANOID_STRIP")
            return re.sub(r'[^a-zA-Z0-9\s]', '', decoded)

        EnterpriseSecurityEngine.log_security_event("XSS", payload, policy, "CLEANED")
        return html.escape(decoded)

    @staticmethod
    def sanitize_sqli(payload: str, policy: int = SecurityLevel.HIGH) -> str:
        if not isinstance(payload, str):
            return ""
        
        decoded = urllib.parse.unquote(payload).strip()
        
        dangerous_sequences = ["--", "/*", "*/", "#", ";"]
        for seq in dangerous_sequences:
            if seq in decoded:
                EnterpriseSecurityEngine.log_security_event("SQLI", payload, policy, "CHAR_STRIP")
                decoded = decoded.replace(seq, "")

        decoded = decoded.replace("'", "''").replace('"', '""')

        sql_patterns = [
            r"\b(UNION\s+SELECT|UNION\s+ALL\s+SELECT)\b",
            r"\b(SELECT|INSERT|UPDATE|DELETE|DROP|ALTER|GRANT|REVOKE|TRUNCATE)\b",
            r"\b(OR|AND)\s+.*?\s*=\s*.*?",
            r"\bHAVING\s+\d+=\d+\b"
        ]
        
        for pattern in sql_patterns:
            if re.search(pattern, decoded, flags=re.IGNORECASE):
                EnterpriseSecurityEngine.log_security_event("SQLI", payload, policy, "KEYWORD_BLOCKED")
                if policy >= SecurityLevel.HIGH:
                    return "[RISK_DETECTED_SQLI_BLOCKED]"
                decoded = re.sub(pattern, "[BLOCKED]", decoded, flags=re.IGNORECASE)
                
        return decoded

    @staticmethod
    def sanitize_os_command(command: str, policy: int = SecurityLevel.HIGH) -> str:
        if not isinstance(command, str):
            return ""
        
        decoded = urllib.parse.unquote(command).strip()
        
        injection_operators = [";", "&&", "||", "|", "`", "$(", ")", "\n", "\r"]
        
        operator_detected = False
        for op in injection_operators:
            if op in decoded:
                operator_detected = True
                if policy >= SecurityLevel.HIGH:
                    EnterpriseSecurityEngine.log_security_event("CMD_INJECTION", command, policy, "COMMAND_BLOCKED")
                    return "[RISK_DETECTED_COMMAND_INJECTION_BLOCKED]"
                decoded = decoded.replace(op, " [OP_BLOCKED] ")
                
        if operator_detected:
            EnterpriseSecurityEngine.log_security_event("CMD_INJECTION", command, policy, "OPERATORS_CLEANED")
            
        return decoded
