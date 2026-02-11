from datetime import datetime
import logging

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


def log_transaction(transaction_type, amount, balance):
    logging.basicConfig(filename="atm_transactions.log", level=logging.INFO)
    logging.info(
        f"{datetime.now()}: {transaction_type} of {amount}. New balance: {balance}"
    )


# ATM withdrawal function real code
def atm_withdrawal(balance, amount):
    current_balance = balance
    amount = float(input("Enter amount: "))
    if amount > current_balance:
        print("Insufficient funds")
    elif amount <= 0:
        print("Invalid amount")
    else:
        current_balance -= amount
        print(f"Withdrawal successful. New balance: {current_balance}")
        log_transaction("withdrawal", amount, current_balance)
        return current_balance


# example usage
current_balance = 5000

# Perform the ATM Withdrawal
atm_withdrawal(current_balance, 0)
log_transaction("withdrawal", 0, current_balance)
