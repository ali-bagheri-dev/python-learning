def login():
    password="0"
    while password!="1234":
        password=input("enter your password")   

def show_menu():
    menuu=int(input("\n 1-balance \n 2-transfer \n 3-withdraw \n 4-exit \n"))
    return menuu

def show_balance(balance):
    print(balance)

def check_card(card_number):
    while len(str(abs(card_number)))!=16:
            print("invalid card number")
            card_number=int(input(" please enter the destination card number\n"))
    return True        
     
def transfer(balance):
    card_number=int(input("enter the destination card number\n"))
    check_card(card_number)
    amount=int(input("enter the amount in toman\n"))
    while amount>balance:
            print("the amount is more than the balance")
            amount=int(input("please enter the amount in toman\n"))
    print("the transfer was successful")
    balance-=amount
    return balance    

def withdraw(balance):
    withdraw=int(input("enter the amount in toman\n"))
    while withdraw>balance:
            print("the amount is more than the balance")
            withdraw=int(input("please enter the amount in toman\n"))
    while withdraw<0:
            print("invalid")
            withdraw=int(input("please enter the amount in toman\n"))
    balance-=withdraw 
    print(f'successful withdraw current balance\n{balance}')
    return balance
balance=10000
login()
while True:
    menu=show_menu()
    if menu==1:
         show_balance(balance)
    elif menu==2:
        balance=transfer(balance)
    elif menu==3:
         balance=withdraw(balance)          
    elif menu==4:
         print("good baye")
         break
