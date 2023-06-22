from classes.BankAccount import BankAccount
from classes.Client import Client

'''
output:
    0 -> want to quit
    1 -> valid input
    2 -> wrong input
'''
def greeting():
    print('--------------------------------')
    print('Hello. What can I help you today?')
    n = input('Please press 1 to insert card or 0 to stop this program\n')
    
    # If the input is not an integer
    if not n.isdigit():
        print(error_msg('invalid'))
        return 2

    # When it is an integer
    choice = int(n)
    if choice == 1:
        return 1
    elif choice == 0:
        print('Thank you. Have a great day')
        return 0
    else:
        print(error_msg('wrong'))
        return 2

def error_msg(n):
    msg = ''
    if n == 'invalid':
        msg += 'Sorry, this is not the right format\n'
    elif n == 'wrong':
        msg += 'Sorry, this is the wrong number\n'
    
    msg += 'We will restart this program\n'
    return msg

'''
This will check the card and PIN number
output:
    Client class if valid
    None if not
'''
def insert_check():
    n = input('\nPlease insert your card (Choose and press the cardID between 1 and 2)\n')
    
    # When cardID is not an integer
    if not n.isdigit():
        print(error_msg('invalid'))
        return None

    # If cardID is an integer but in wrong range
    cardID = int(n)
    if (cardID < 1 or cardID > 2):
        print(error_msg('wrong'))
        return None

    client = card_client[cardID]
    # We have 3 chances to enter the PIN
    for i in range(3):
        print('\nPlease enter the PIN Number (4 digits)')
        m = input('')

        # If the PIN is not an integer
        if not m.isdigit():
            print('Sorry, this is not the right format for PIN\n')
        
        else:
            # If the PIN is an integer but in wrong range
            if int(m) != client.getPW():
                print('Sorry, this is a wrong PIN\n')
            
            # If the PIN is right
            else:
                return client
    
    return None

'''
Select account and see balance/deposit/withdraw
output:
    1 if user wants to quit
    0 if the input is invalid/wrong
'''
def deal_account(client):
    print(f'\nHello, {client.getLastName()}. Please select the "account number"')
    accounts_num = client.getAllAccounts()
    for i, account_num in enumerate(accounts_num):
        print(f'{i+1}. {account_num}')
    n = input('')
    
    if not n.isdigit():
        print(error_msg('invalid'))
    
    else:
        if int(n) not in accounts_num:
            print(error_msg('wrong'))
        
        else:
            account = client.getAccount(int(n))
            print(f'\nSelected Account Number: {account.getAccountNum()}')
            while True:                
                print('Please press the number for the next action or select 0 to stop this program')
                print('0 => Quit')
                print('1 => See Balance')
                print('2 => Deposit')
                print('3 => Withdraw')
                next = input('')
                if not next.isdigit():
                    print(error_msg('invalid'))
                    continue

                next = int(next)
                if next < 0 or next > 3:
                    print(error_msg('wrong'))
                    continue

                if next == 0:
                    print('Thank you')
                    return 1
                
                elif next == 1:
                    print(f'\nCurrent Balance: ${account.getBalance()}\n')
                    continue

                elif next == 2:
                    prev_balance = account.getBalance()
                    print("\nEnter the amount to deposit into the account")
                    amount = int(input())
                    account.deposit(amount)
                    print(f'Before you deposit: ${prev_balance}')
                    print(f'After you deposit: ${account.getBalance()}\n')
                    continue

                elif next == 3:
                    prev_balance = account.getBalance()
                    print('\nEnter the amount to withdraw from the account')
                    amount = int(input())
                    result = account.withdraw(amount)
                    if result == -1:
                        print("Failed. Please check the current balance\n")
                        continue
                    print(f'Before you deposit: ${prev_balance}')
                    print(f'After you deposit: ${account.getBalance()}\n')
                    continue
                    
    return 0

if __name__ == '__main__':
    # accounts in client 1
    account1 = BankAccount(111111111)
    account1.deposit(300)
    account2 = BankAccount(222222222)
    account2.deposit(500)
    client1 = Client('Michel', 'Lee', 7777)
    client1.setAllAccounts([account1, account2])

    # accounts in client 2
    account3 = BankAccount(333333333)
    account3.deposit(700)
    client2 = Client('Paul', 'Park', 8888)
    client2.setAccount(account3)

    card_client = {1: client1, 2: client2}
    
    while True:
        # n = 0 => quit
        # n = 1 => valid input
        # n = 2 => wrong input
        n = greeting()
        if n ==  0:
            break
        elif n == 2:
            continue
        else:
            # client is None => Invalid/Wrong PIN Number
            # client is not None => PIN Number OK
            client = insert_check()
            if client is None:
                continue
            else:
                # result = 1 => quit
                quit = deal_account(client)
                if quit == 1:
                    break

        
