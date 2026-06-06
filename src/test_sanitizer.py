import unittest
from src.sanitizer import EnterpriseSecurityEngine, SecurityLevel

class TestEnterpriseSecurityEngine(unittest.TestCase):
    
    def test_xss_sanitization(self):
        payload = "<script>alert(1)</script>"
        result = EnterpriseSecurityEngine.sanitize_xss(payload)
        self.assertNotIn("<script>", result)

    def test_sqli_sanitization(self):
        payload = "admin' OR '1'='1"
        result = EnterpriseSecurityEngine.sanitize_sqli(payload)
        self.assertEqual(result, "BLOCK_ALERT")

    def test_rce_shield(self):
        payload = "127.0.0.1 ; whoami"
        result = EnterpriseSecurityEngine.sanitize_os_command(payload)
        self.assertEqual(result, "ERROR_TRACKING_FLAG")

    def test_url_validation(self):
        self.assertTrue(EnterpriseSecurityEngine.validate_url("https://owasp.org"))
        self.assertFalse(EnterpriseSecurityEngine.validate_url("http://localhost/admin"))
        self.assertFalse(EnterpriseSecurityEngine.validate_url("javascript:alert(1)"))

    def test_email_validation(self):
        self.assertTrue(EnterpriseSecurityEngine.validate_email("atahan@istinye.edu.tr"))
        self.assertFalse(EnterpriseSecurityEngine.validate_email("invalid-email@com"))

    def test_file_validation(self):
        self.assertTrue(EnterpriseSecurityEngine.validate_file("report.json"))
        self.assertFalse(EnterpriseSecurityEngine.validate_file("../../../etc/passwd"))
        self.assertFalse(EnterpriseSecurityEngine.validate_file("malicious.exe"))

if __name__ == '__main__':
    unittest.main()
