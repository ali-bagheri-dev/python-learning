def show_menu():
    choise=int(input("1-Add contact\n2-Show contact\n3-Exit\n"))
    return choise
def add_contact():
    name=input('enter name: ')    
    number=input('enter number: ')
    with open('contacts.txt','a') as file:
        file.write(f"{name},{number}\n")
    print('successful')    
def show_contact():
    with open('contacts.txt','r') as file:
        text=file.read()        
    print(text) 
while True:
    menu=show_menu()    
    if menu==1:
        add_contact()
    elif menu==2:
        show_contact()
    elif menu==3:
        print('goodbye')       
        break
