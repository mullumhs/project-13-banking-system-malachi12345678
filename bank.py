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

    def add_account(self , account, acount_holder , account_password):
        new_account = Account()
        
        
        
        self.accounts.append(account)
