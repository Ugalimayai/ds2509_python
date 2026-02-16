# Python script/file to demonstrate the use of instance, static and class methods
# in a real world scenario

#import the regular expressions module
import re

# your password must be 8 or more characters, have at least 1 lowercase, 1 uppercase, 1 number, and a special character

class BankAccount:
    #Class attribute (shared across all instances)
    interest_rate = 0.05 #5% annual interest rate

    #constructor
    def __init__(self, account_holder, balance = 0.0):
        self.account_holder = account_holder
        self.balance = balance

    # -----------------------------------------------------------------
    #instance method(s)
    # -----------------------------------------------------------------
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            #display the new balance
            print(f"[{self.account_holder}] deposited Kes.{amount:.2f}."
                  f"\nBalance: {self.balance:.2f}")
        else:
            print(f"Kindly note that the deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount: # can be shortened to [if 0 > amount <= self.balance:]

            self.balance -= amount # to make it more realistic, deduct relevant bank charges
            # display the amount withdrawn and new balance
            print(f"[{self.account_holder}] withdrew Kes.{amount:.2f}."
                  f"\nNew balance is: {self.balance:.2f}")
        else:
            print(f"Invalid withdrawal amount or insufficient funds. Try again.")


    #-----------------------------------------------------------------
    # Class Method(s)
    # -----------------------------------------------------------------
    @classmethod
    def set_interest_rate(cls, new_rate):
        if 0 < new_rate < .2:
            cls.interest_rate = new_rate
        # Notify about the change in annual interest rate
            print(f"The annual interest rate has been set to {new_rate * 100 :.2f}% for all accounts.")
        else:
            print(f"The annual interest rate must be between 0.0% and 20.0%!")

    # -----------------------------------------------------------------
    # Static method(s)
    # -----------------------------------------------------------------
    @staticmethod
    def validate_account_number(account_number):
        pattern = r"^ACC\d{6}$" #regular expression (regex) pattern to ensure the account starts with ACC followed by 6 digits
        return bool(re.match(pattern, account_number))

# -----------------------------------------------------------------
# Demonstrate the bankAccount class and its static, instance and class methods
# -----------------------------------------------------------------

#create 2 bank accounts => using the constructor
chris_acc = BankAccount("CHRIS", 129000.00)
brian_acc = BankAccount("BRIAN", 10000.00)

#deposit and withdraw money into and from the bank account => instance methods
chris_acc.deposit(1500)
brian_acc.withdraw(70000)

#update the annual interest rate from 5% to 8% =>  using the class method
BankAccount.set_interest_rate(.08)

#validate the new account numbers => static method
print("Validating  new account numbers...\nPlease wait...")
print(f"ACC123457 is valid? {BankAccount.validate_account_number('ACC123457')}")
print(f"Account321547 is valid? {BankAccount.validate_account_number('ACC321547')}")

