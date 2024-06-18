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

    def print_account_list(self):
        print(self.accounts)
    


manager = Bank()
manager.add_account(123123 , "gregory", "eggory")
manager.print_account_list()