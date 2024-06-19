""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self , account_number , account_holder , account_password):
        account = Account(  account_number , account_holder , account_password)
        self.accounts.append(account)

    def remove_account(self , removed_account_number):
        for account in self.accounts:
            if account.get_account_number() == removed_account_number:
                self.accounts.remove(account)
                print(f"removed account {removed_account_number}")
             


    def print_all(self):
        for account in self.accounts:
            print(account)
    
    


manager = Bank()
manager.add_account(123123 , "gregory", "eggory")
manager.add_account(232344 , "john", "asdfsif")
manager.print_all()
manager.remove_account(123123)
manager.print_all()