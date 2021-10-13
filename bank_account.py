from credit_card import CreditCard

# Here is something like a Database! (Credit cards will define here).

babak = CreditCard('babak',6663,750)
mehrad = CreditCard('mehrad',2250,2500)
saeed = CreditCard('saeed',7623,340)
mehran = CreditCard('mehran',1351,102000)

creditcards = [babak,mehrad,saeed,mehran]
creditcards_dict = {'babak':babak, 'mehrad':mehrad, 'saeed':saeed, 'mehran':mehran}
# Write your code here...



print('''
Welcome to The city bank App.
You can do your banking like transfer, withdraw, deposit and other bank things in here.
you can contact our support in 24/7. https://t.me/Babakzaree
''')
print("Please Log in.")


while True:
    username = input("Username: ")
    currect_user_index = None

    password = int(input('Password: '))
    currect_pass_index = None

    user_correct = False
    pass_correct = False

    loop1 = 0
    while loop1 < len(creditcards):
        if username == (creditcards[loop1].name):
            currect_user_index = loop1
            user_correct = True
            break
        loop1 += 1

    loop2 = 0
    while loop2 < len(creditcards):
        if password == (creditcards[loop2].password):
            currect_pass_index = loop2
            pass_correct = True
            break
        loop2 += 1
    if (user_correct == True) and (pass_correct == True):    
        print("Hello {}. Welcome to your account.".format(username))
        print('\nwhat you want to do?')
        
        user_credit = (creditcards[currect_user_index])
        
        log_in = True
        
        while log_in == True:
            user_input = input('''
            '1' for Balance
            '2' for Deposit
            '3' for Withdraw
            '4' for Transfer to another account
            'logout' for Loging out
            'quit' for quit the App
            Type Here: ''')    
            
            if user_input.lower() not in ('1','2','3','4','logout','quit'):
                print('\'{}\' is invalid command.'.format(user_input))

            if user_input.lower() == 'logout':
                print("Logged out successfuly.")
                log_in = False
                break
            
            if user_input.lower() == 'quit': # if user wanted to quit the app
                exit_the_app = True
                print("Quited succesfuly.")
                exit()
            
            if user_input == '1':  # Code for showing balance of Credit card
                print(f'\n\'\'Your Balance is: {user_credit.credit_balance()}$\'\'\n')
            
            
            if user_input == '2':
                deposit_amount = int(input('Enter the amount that you want to deposit: '))
                user_credit.deposit(deposit_amount)
                print(f"\'\'\'Deposited {deposit_amount}$\'\'\'")
            
            
            if user_input == '3':
                withdraw_amount = int(input('Enter the amount that you want to withdraw: '))
                user_credit.withdraw(withdraw_amount)
                print(f"\'\'\'Withdrawed {withdraw_amount}$\'\'\'")
            

            if user_input == '4':
                transfer_amount = int(input('Enter how much money do you want to transfer: '))
                transfer_to = input('Ok. Now enter name of person That you want Transfer money for it: ')
                
                user_credit.transfer(transfer_amount, creditcards_dict[transfer_to])
                print(f'Transfered {transfer_amount}$ to {transfer_to}\'s Credit card.')
    
    else:
        print("this username/password Combination is invalid.")
        ask_user = input("Do you want to close the app? enter 'y' for exit Or enter any chars for continue: ")
        if ask_user.lower() == 'y':
            exit()