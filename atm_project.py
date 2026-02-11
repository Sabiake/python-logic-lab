import logging
from datetime import datetime

# Sample atm pseudocode
# 1. Start
# 2. Initialize current_balance
# 3. Display menu options
# 4. Get user choice
# 5. If choice is withdrawal:
#      a. Get withdrawal amount
#      b. Call atm_withdrawal(current_balance, withdrawal_amount)
# 6. If choice is deposit:
#      a. Get deposit amount
#      b. Call atm_deposit(current_balance, deposit_amount)
# 7. End

# 1. Set-up a professional logging

logging.basicConfig(
    filename="atm_transactions.log",
    level=logging.INFO,
    format="%(asctime)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# ATM withdrawal function real code
def atm_withdrawal(balance):
    """Handles ATM withdrawal logic and returns the updated balance."""
    try:
        # Prompt user inside the function since we need fresh input
        amount_str = input("\nEnter amount to withdraw: ")
        amount = float(amount_str)

        # 2. Logical checks
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
            return balance

        if amount > balance:
            print(f"Insufficient funds. Your current balance is ${balance:.2f}")
            return balance

        # 3. Successful transaction
        new_balance = balance - amount
        print(f"Withdrawal successful. New balance: KES{new_balance:.2f}")

        # This logs using the logging module instead of manual file writing
        logging.info(f"Withdrawal of {amount}. New balance: {new_balance}")

        return new_balance

    except ValueError:
        # 4. Handle non-numeric input (e.g., if user types "abc") just for better error handling
        print("Error: Please enter a valid numerical amount.")
        return balance


# Example usage / Perform the ATM Transaction
def main():
    current_balance = 5000.0
    print("--- Welcome to my 2026 Python ATM ---")

    while True:
        print(f"\nCurrent Balance: KES{current_balance:.2f}")
        choice = input("1. Withdraw\n2. Exit\nSelect option: ")

        if choice == "1":
            # 5. Capture the return value to update the global balance
            current_balance = atm_withdrawal(current_balance)
        elif choice == "2":
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()
