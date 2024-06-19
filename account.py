""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Account:
    def __init__(self , account_number , account_holder , account_password):
        self._account_balance = 0        
        self.set_account_holder(account_holder)
        self.set_account_number(account_number)
        self.set_account_password(account_password)
        
    def __str__(self):
        return f"{self._account_number} {self._account_holder} {self._account_balance} {self._account_password}"
    

    def get_account_number(self):
        return self._account_number

    def get_account_holder(self):
        return self._account_holder 

    def get_account_password(self):
        return self._account_password

    def get_account_balance(self):
        return self._account_balance


    def set_account_number(self , new_account_number):
        if new_account_number == "":
            raise ValueError("number must not be empty")
        self._account_number = new_account_number

    def set_account_holder(self , new_account_holder):
        if new_account_holder == "":
            raise ValueError("name must not be empty")
        self._account_holder = new_account_holder

    def set_account_password(self , new_account_password):
        if new_account_password == "":
            raise ValueError("password must not be empty")
        self._account_password = new_account_password

    def set_account_balance(self , new_account_balance):
        if new_account_balance < 0:
            raise ValueError("balance must not be negative")
        self._account_balance = new_account_balance

    def deposit(self , deposit_ammount):
        if deposit_ammount <= 0:
            raise ValueError("transfer must not be negative")
        self._account_balance += deposit_ammount
    
    def withdraw(self , withdraw_ammount):
        if withdraw_ammount > self._account_balance:
            raise ValueError("withdraw cannot be more than balance")
        self._account_balance -= withdraw_ammount


