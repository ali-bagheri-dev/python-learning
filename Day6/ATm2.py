balance=10000
password=1435
exit=0
login_password=int(input("enter your password "))
def login(login_passwor):
    while password!=login_password:
         print("invalid password")
    login_password=input("please enter your password ")
def show_menu():
    menu=int(input("\n 1-balance \n 2-transfer \n 3-withdraw \n 4-exit \n"))
    return menu
def check_card(card_number):
    while len(str(abs(card_number)))!=16:
            print("invalid card number")
            card_number=int(input(" please enter the destination card number\n"))
     
     
def balance():
    print(f'{balance}toman')
def transfer():
     card_number=int(input("enter the destination card number\n"))
     if check_card(card_number)==True: 
         amount=int(input("enter the amount in toman\n"))
     while amount>balance:
            print("the amount is more than the balance")
            amount=int(input("please enter the amount in toman\n"))
     print("the transfer was successful")
     balance-=amount
     print(f'current balance: {balance}')


while exit!=1:
    menu=show_menu()
    if menu==1:
         balance()
        
    elif menu==2:
        transfer()
    elif menu==3:
        withdraw=int(input("enter the amount in toman\n"))
        while withdraw>balance:
            print("the amount is more than the balance")
            withdraw=int(input("please enter the amount in toman\n"))
        while withdraw<0:
            print("invalid")
            withdraw=int(input("please enter the amount in toman\n"))
        balance-=withdraw 
        print(f'successful withdraw current balance\n{balance}')
    elif menu==4:
        print("take your card")
        exit=1
    else:
        print('invalid menu')


    
