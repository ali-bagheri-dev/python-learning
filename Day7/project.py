contact=[]
def show_menu():
    menu1=int(input("1_add name\n2_print names\n3_serch\n4_delete\n5_exit\n"))
    return menu1
def input_name():
    enter_name=input('enter contact name: ')
    enter_name=enter_name.lower()
    return enter_name.title()

def add_contact(name):
    contact.append(name)
    
def print_contact():
    i=0
    for name in contact:
        i=i+1
        print(i,'-',name)

def search(name):
    if name in contact:
        print('found')
    else:
        print('not found')

def delete(name):
    if name in contact:
        contact.remove(name)
    else:
        print('not found')    
            
while True:
    menu=show_menu()
    if menu==1:
        name=input_name()
        add_contact(name)
    elif menu==2:
        print_contact()
    elif menu==3:
        name=input_name()
        search(name)
    elif menu==4:
        name=input_name()
        delete(name)
    elif menu==5:
        print('goodbye')    
        break
