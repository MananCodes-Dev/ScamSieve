# ScamSieve 🔎

**A beginner-friendly Python application that identifies configured warning signs in suspicious messages.**

ScamSieve analyzes text messages using simple, rule-based keyword matching. It highlights phrases associated with urgency, financial requests, sensitive information, and suspicious links.

The project was built to practice Python programming, regular expressions, automated testing, Git, and desktop application development.

> **Important:** ScamSieve is an educational project, not a definitive scam detector. A warning does not prove that a message is fraudulent, and no warning does not mean a message is safe.

## Features

- **Urgency detection:** Identifies phrases such as `urgent`, `immediately`, and `act now`.
- **Financial-request detection:** Flags configured phrases such as `send money`, `payment required`, and `pay now`.
- **Sensitive-information warnings:** Detects configured requests involving OTPs, passwords, and PINs.
- **Suspicious-link warnings:** Flags configured patterns, including HTTP/HTTPS URLs and popular URL-shortening domains.
- **Matched-phrase explanations:** Shows which configured phrases triggered each warning category.
- **Desktop GUI:** Provides a text input area, an Analyze Message button, results, and a Clear button.
- **Input validation:** Rejects empty messages and non-string inputs in the analysis function.
- **Automated tests:** Uses Python's built-in `unittest` framework to verify expected behavior.

## Requirements

- Python 3.10 or later recommended
- Windows, macOS, or Linux with Tkinter available for the desktop interface
- Git (optional, for cloning the repository)

No third-party Python packages are required by the current application code.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MananCodes-Dev/ScamSieve.git
cd ScamSieve
```

### 2. Create a virtual environment (recommended)

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Run the command-line version

```bash
python src/scamsieve.py
```

Paste a message when prompted to see the analysis results.

### 4. Run the desktop application

```bash
python -m src.gui
```

Paste a message into the input area and select **Analyze Message**. Use **Clear** to reset the input and results.

## Run the Tests

From the project root, execute:

```bash
python -m unittest discover -s tests -v
```

The current test suite contains 10 tests covering:

- Urgent-language detection
- Sensitive-information detection
- Multiple warning categories
- HTTP/HTTPS and shortened-link warning patterns
- Matched-phrase reporting
- Normal messages without configured warning signs
- Empty and invalid input
- Keyword boundary behavior

The test suite passed locally during development. Run it yourself to verify the current checkout.

## Project Structure

```text
ScamSieve/
├── src/
│   ├── scamsieve.py
│   └── gui.py
├── tests/
│   └── test_scamsieve.py
├── README.md
└── .gitignore
```

- `src/scamsieve.py` — warning rules, message analysis, and command-line interface.
- `src/gui.py` — Tkinter desktop interface.
- `tests/test_scamsieve.py` — automated tests for the analysis function.

## Limitations

ScamSieve uses predefined keyword rules rather than machine learning or a threat-intelligence service.

- It can miss scams that use unfamiliar wording or unconfigured patterns.
- It can flag legitimate messages that contain warning phrases.
- It does not understand context, sender identity, or the intent behind a message.
- It does not verify whether a URL is malicious or safe.
- An HTTPS URL is not necessarily trustworthy.
- It does not connect to external security databases or perform real-time threat analysis.

**Never share an OTP, password, PIN, or other sensitive information simply because a message appears legitimate. Verify suspicious requests through an independently obtained official contact channel.**

## Learning Goals

This project helped me practice:

- Python functions, dictionaries, loops, and exception handling
- Regular expressions and text normalization
- Writing automated unit tests
- Separating application logic from the graphical interface
- Git branching, commits, merging, and GitHub collaboration workflows
- Documenting software behavior and limitations

## Future Improvements

Potential next steps include:

- Improving URL parsing and detection tests
- Adding configurable warning rules
- Improving the GUI's visual design and accessibility
- Adding more test cases for false positives and false negatives
- Evaluating detection performance against a documented test dataset

## Author

**Manan Kumar**

GitHub: [@MananCodes-Dev](https://github.com/MananCodes-Dev)

Repository: [ScamSieve](https://github.com/MananCodes-Dev/ScamSieve)

---

*Built as a learning project to explore Python development and basic cybersecurity concepts.*
