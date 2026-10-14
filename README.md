
# ScamSieve

ScamSieve is a beginner-friendly Python project that identifies
basic warning signs in suspicious messages.

## Features

- Detects urgent language.
- Identifies requests for sensitive information.
- Flags certain suspicious link patterns.
- Includes automated tests.

## Run the project

```bash
python src/scamsieve.py
```

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## Limitations

ScamSieve uses simple keyword rules. It can miss scams and flag
legitimate messages. It cannot determine whether a message is safe.
