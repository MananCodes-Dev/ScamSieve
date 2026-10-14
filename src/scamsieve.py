
def analyze_message(message):
    """Identify basic warning signs in a suspicious message."""
    warning_signs = {
        "urgent language": ["urgent", "immediately", "act now"],
        "financial requests": ["send money", "payment required"],
        "sensitive information": ["share otp", "password", "pin"],
        "suspicious links": ["http://", "bit.ly", "tinyurl.com"],
    }

    findings = []

    message_lower = message.lower()

    for category, keywords in warning_signs.items():
        for keyword in keywords:
            if keyword in message_lower:
                findings.append(category)
                break

    return findings


def main():
    message = input("Paste a message to analyze: ")
    findings = analyze_message(message)

    print("\n--- ScamSieve Analysis ---")

    if findings:
        print("Warning signs detected:")
        for finding in findings:
            print(f"- {finding}")
    else:
        print("No configured warning signs detected.")

    print("\nThis tool cannot confirm whether a message is safe.")


if __name__ == "__main__":
    main()
