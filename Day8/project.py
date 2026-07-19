contacts = [
    {'name': 'Ali', "phone": "111"},
    {'name': 'Sara', "phone": "222"},
    {'name': 'Reza', "phone": "333"}
]

def show_menu():
    choice=int(input("1_add contact\n2_Show Contacts\n3_Search by Name\n4_Delete Contact\n5_exit\n"))
    return choice

def add_contact(name,number):
    contact={
        'name':name,
        'phone':number
    }
    contacts.append(contact)
    with open('contacts.txt','a') as file:
        file.write('name:',contact['name'],'\nphone:',contact['phone'],'\n-------------')

    print("It was successful.")

def input_name():
    enter_name=input('enter contact name: ')
    enter_name=enter_name.lower()
    return enter_name.title()

def input_phone():
    enter_phone=input('enter number: ')
    return enter_phone

def print_contact():
    for contact  in contacts:
        print('name:',contact['name'],'\nphone:',contact['phone'],'\n-------------')
        
        
def search(name):
    for contact in contacts:
        if name == contact['name']:
           return(contact['phone'])
    return('not found')

def delete(name):
    for contact in contacts:
        if name == contact['name']:
            contacts.remove(contact)  
            return("It was successful.")
                   
    return('not found')
        

while True:
    menu=show_menu()
    if menu==1:
        name=input_name()
        number=input_phone()
        add_contact(name,number)
    elif menu==2:
        print_contact()
    elif menu==3:
        name=input_name()
        print(search(name))

    elif menu==4:
        name=input_name()
        print(delete(name))
    elif menu==5:
        print('goodbye')    
        break