class CreditCard:
    
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance
    
    def credit_balance(self):
        '''Return Balance of credit card'''
        return self.balance
    def deposit(self,amount):
        '''Deposit given amount to credit card balance.'''
        self.balance +=  amount
        return "Deposited Successfuly. Balance:{}".format(self.balance)
    
    def withdraw(self,amount):
        '''withdraw given amount from credit card balance.'''
        if (self.balance - amount) < 5:
            print("Not enough cash.")
            return
        self.balance -= amount
        return "Withdrawed Successfuly. Balance: {}".format(self.balance)
    
    def transfer(self,amount,credit_name):
        '''Transfer Given amount to another Credit card'''  
        if (self.balance-amount) < 5:
            print('Not enough cash.')
            return
        self.balance -= amount
        credit_name.deposit(amount)
        return'Transeferd Successfuly. Balance:{}'.format(self.balance)
        
    def __str__(self):  
        return f"CreditCard(Name: {self.name}, Balance: {self.balance})"