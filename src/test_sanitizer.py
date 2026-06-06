import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sanitizer import EnterpriseSecurityEngine, SecurityLevel

class TestEnterpriseSecurityEngine(unittest.TestCase):

    def test_xss_mitigation(self):
        bad_input = "<script>alert('Hacked')</script>"
        clean = EnterpriseSecurityEngine.sanitize_xss(bad_input, policy=SecurityLevel.HIGH)
        self.assertNotIn("<script>", clean)
        
        mixed_input = "<sCrIpT>prompt(1)</ScRiPt>"
        clean_mixed = EnterpriseSecurityEngine.sanitize_xss(mixed_input, policy=SecurityLevel.HIGH)
        self.assertNotIn("<sCrIpT>", clean_mixed)
        
        event_input = "<img src=x onerror=alert(1)>"
        clean_event = EnterpriseSecurityEngine.sanitize_xss(event_input, policy=SecurityLevel.HIGH)
        self.assertNotIn("onerror", clean_event)

    def test_sqli_mitigation(self):
        sqli_input = "admin' OR '1'='1"
        clean = EnterpriseSecurityEngine.sanitize_sqli(sqli_input, policy=SecurityLevel.HIGH)
        self.assertNotIn("'", clean)
        self.assertEqual(clean, "[RISK_DETECTED_SQLI_BLOCKED]")
        
        union_input = "1 UNION SELECT username, password FROM users"
        clean_union = EnterpriseSecurityEngine.sanitize_sqli(union_input, policy=SecurityLevel.HIGH)
        self.assertEqual(clean_union, "[RISK_DETECTED_SQLI_BLOCKED]")

    def test_os_command_mitigation(self):
        cmd_input = "127.0.0.1 ; cat /etc/passwd"
        clean = EnterpriseSecurityEngine.sanitize_os_command(cmd_input, policy=SecurityLevel.HIGH)
        self.assertEqual(clean, "[RISK_DETECTED_COMMAND_INJECTION_BLOCKED]")
        
        cmd_input_and = "8.8.8.8 && whoami"
        clean_and = EnterpriseSecurityEngine.sanitize_os_command(cmd_input_and, policy=SecurityLevel.HIGH)
        self.assertEqual(clean_and, "[RISK_DETECTED_COMMAND_INJECTION_BLOCKED]")

if __name__ == "__main__":
    unittest.main()
