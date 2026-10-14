
import unittest

from src.scamsieve import analyze_message


class TestScamSieve(unittest.TestCase):

    def test_detects_urgent_language(self):
        findings = analyze_message("URGENT! Act now")
        self.assertIn("urgent language", findings)

    def test_detects_sensitive_information(self):
        findings = analyze_message("Please share OTP")
        self.assertIn("sensitive information", findings)

    def test_normal_message_has_no_warning_signs(self):
        findings = analyze_message("Your class starts at 10 AM")
        self.assertEqual(findings, [])

    def test_detects_multiple_warning_signs(self):
        findings = analyze_message(
            "URGENT! Share OTP immediately"
        )
        self.assertIn("urgent language", findings)
        self.assertIn("sensitive information", findings)


if __name__ == "__main__":
    unittest.main()
