
import re


WARNING_RULES = {
    "urgent language": [
        "urgent",
        "immediately",
        "act now",
        "within 24 hours",
    ],
    "financial requests": [
        "send money",
        "payment required",
        "pay now",
    ],
    "sensitive information": [
        "share otp",
        "one time password",
        "share your password",
        "share your pin",
    ],
    "suspicious links": [
        "http://",
        "https://",
        "bit.ly",
        "tinyurl.com",
    ],
}


def analyze_message(message):
    """Return warning categories and the phrases that triggered them."""

    if not isinstance(message, str):
        raise TypeError("Message must be a string.")

    if not message.strip():
        raise ValueError("Message cannot be empty.")

    normalized_message = message.lower()
    findings = []

    for category, keywords in WARNING_RULES.items():
        matched_phrases = []

        for keyword in keywords:
            pattern = r"\b" + re.escape(keyword) + r"\b"

            if re.search(pattern, normalized_message):
                matched_phrases.append(keyword)

        if matched_phrases:
            findings.append({
                "category": category,
                "matched_phrases": matched_phrases,
            })

    return findings


def main():
    print("=== ScamSieve ===")
    print("Analyze a message for configured warning signs.")
    print("This tool cannot confirm whether a message is safe.\n")

    message = input("Paste a message: ")

    try:
        findings = analyze_message(message)
    except (TypeError, ValueError) as error:
        print(f"\nInput error: {error}")
        return

    print("\n=== Analysis Results ===")

    if not findings:
        print("No configured warning signs detected.")
    else:
        for finding in findings:
            print(f"\nCategory: {finding['category']}")
            print("Matched phrases:")

            for phrase in finding["matched_phrases"]:
                print(f"  - {phrase}")

    print("\nReminder: this is a basic rule-based tool,")
    print("not a definitive scam detector.")


if __name__ == "__main__":
    main()
