
import unittest

from src.scamsieve import analyze_message


class TestScamSieve(unittest.TestCase):

    def test_detects_urgent_language(self):
        findings = analyze_message("URGENT! Act now")
        categories = [item["category"] for item in findings]

        self.assertIn("urgent language", categories)

    def test_detects_sensitive_information(self):
        findings = analyze_message("Please share OTP")
        categories = [item["category"] for item in findings]

        self.assertIn("sensitive information", categories)

    def test_normal_message_has_no_warning_signs(self):
        findings = analyze_message("Your class starts at 10 AM")

        self.assertEqual(findings, [])

    def test_detects_multiple_warning_signs(self):
        findings = analyze_message("URGENT! Share OTP immediately")
        categories = [item["category"] for item in findings]

        self.assertIn("urgent language", categories)
        self.assertIn("sensitive information", categories)

    def test_returns_matched_phrases(self):
        findings = analyze_message("Payment required immediately")

        all_phrases = [
            phrase
            for item in findings
            for phrase in item["matched_phrases"]
        ]

        self.assertIn("payment required", all_phrases)
        self.assertIn("immediately", all_phrases)

    def test_rejects_empty_message(self):
        with self.assertRaises(ValueError):
            analyze_message("   ")

    def test_rejects_non_string_input(self):
        with self.assertRaises(TypeError):
            analyze_message(None)

    def test_detects_shortened_link(self):
        findings = analyze_message(
            "Claim your reward at https://bit.ly/example"
        )
        categories = [item["category"] for item in findings]

        self.assertIn("suspicious links", categories)

    def test_ignores_keyword_inside_larger_word(self):
        findings = analyze_message("This is an urgency exercise.")
        categories = [item["category"] for item in findings]

        self.assertNotIn("urgent language", categories)

    def test_detects_https_link(self):
        findings = analyze_message(
            "Verify your account at https://example.com"
        )
        categories = [item["category"] for item in findings]

        self.assertIn("suspicious links", categories)


if __name__ == "__main__":
    unittest.main()
