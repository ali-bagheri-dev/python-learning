#name karbari
User_Name= "Ali"
Password="123"
u_name=input("User Name ")
if u_name.title()==User_Name:
    Pas=input("Enter password ")
    if Pas==Password:
        print("Welcome Ali")
    else:
        print("Password is incorrect")    
else:
    print("Username is incorrect")    