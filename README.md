# python-logic-lab

Mini python solutions

# Python Logic Lab: Practical Scripts & Mini-Apps

A collection of lightweight Python projects demonstrating core programming logic,
problem-solving, and automation. This repository showcases my ability to bridge
technical code with real-world scenarios—from ATM simulations to data processing tools.

### Featured Scripts

- **ATM Simulation:** A robust terminal-based app with transaction logging and error handling.

# ATM Mini Project

Short description

- Small CLI ATM simulator that supports withdrawals.
- Core file: `atm_project.py`. Tests live in `test_atm.py`.
- Designed for learning I/O, basic validation, logging and unit testing with mocks.

Files

- atm_project.py — main program and function `atm_withdrawal(balance)`:
  - Prompts user for an amount via input()
  - Validates numeric/positive/available funds
  - Prints result messages and returns the updated balance (float)
  - Logs transactions to `atm_transactions.log`
- test_atm.py — unit tests that:
  - Mock `builtins.input` to simulate user input
  - Capture `sys.stdout` to assert printed messages
  - Assert returned balance values

Requirements

- Python 3.8+
- No external packages required

How to run the program (Windows)

- From project folder:
  - python atm_project.py
- Interact via the menu; choose "1" to withdraw and follow prompts.

How to run tests (Windows)

- From project folder:
  - python -m unittest c:\Users\sabia_kenya\Desktop\LearningPython_Basics\test_atm.py

Notes about tests

- Tests do not modify `atm_project.py`. They mock `input()` and capture stdout so the I/O code can be tested without changing the source.
- Tests assert:
  - Correct updated balance returned by `atm_withdrawal`
  - Presence of expected printed messages (e.g., "Withdrawal successful", "Insufficient funds", "Invalid amount", and numeric-input error message)

Suggestions for future improvements

- Separate business logic from I/O: create functions like `process_withdrawal(balance, amount)` that only implement logic and return (new_balance, message). This simplifies testing (no mocking).
- Add deposit functionality and persistence (file or DB) if desired.
- Add a `reset_balance()` helper or class-based ATM to isolate state across tests.

Logging

- Transactions are appended to `atm_transactions.log` in the project directory with timestamps (configured in `atm_project.py`).

---

- **Network Port Scanner:** A multi-threaded utility that probes specific IP addresses for open ports. It demonstrates knowledge of the `socket` library, TCP handshakes, and network diagnostics—essential for technical SEO and web security audits.
- **Data Utility Tools:** Scripts designed to clean and prep data for Excel & Power BI.
- **AI & API Experiments:** Exploring rapid tech innovations through integrated Python libraries.

### Tech Stack

- **Language:** Python 3.12+
- **Core Libraries:** `datetime`, `logging`, `math`, `sys`, `socket`, `threading`,`unittest`,`unittest.mock` ,`io`
- **Concepts:** Error Handling (Try/Except), File I/O, Data Validation, and Functional Programming.

---

_Building at the intersection of Data, Marketing, and Code._
