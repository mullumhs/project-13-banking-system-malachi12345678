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

    def remove_account(self , remove_account_number):
        for account in self.accounts:
            if account.get_account_number() == remove_account_number:
                self.accounts.remove(account)
                print(f"removed account {remove_account_number}")
             
    def deposit(self , deposit_account_number , deposit_ammount):
        for account in self.accounts:
            if account.get_account_number() == deposit_account_number:
                account.deposit(deposit_ammount)

    def withdraw(self , withdraw_account_number , withdraw_ammount):
        for account in self.accounts:
            if account.get_account_number() == withdraw_account_number:
                account.withdraw(withdraw_ammount)

    def transfer(self , withdraw_account_number , deposit_account_number , transfer_ammount):
        for account in self.accounts:
            if account.get_account_number() == withdraw_account_number:
                account.withdraw(transfer_ammount)        
                
        for account in self.accounts:
            if account.get_account_number() == deposit_account_number:
                account.deposit(transfer_ammount)





    def print_all(self):
        for account in self.accounts:
            print(account)
    
    


#manager = Bank()
#manager.add_account(123123 , "gregory", "eggory")
#manager.add_account(232344 , "john", "asdfsif")
#manager.add_account(333434 , "pluh", "23231")
#manager.print_all()
#manager.print_all()
#manager.deposit(232344 , 234)
#manager.deposit(123123 , 100)
#manager.deposit(33434 , 100)
#manager.print_all()
#manager.withdraw(232344 , 100)
#manager.transfer(123123 , 232344 , 100)
#manager.print_all()