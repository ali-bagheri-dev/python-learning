def say_hello(name):
    print(f"Hello {name}")
say_hello("ali")

def square(number):
    print(number*number)
square(5)    

def if_even(number):
    if number%2==0:
        return True
    else:
        return False
    
print(if_even(9))    

def calculate_age(birth_year):
    print(2026-birth_year)
calculate_age(2002)


def login(username,password):
    return username=="Ali" and password=="1234"
        
#use=input("pleas enter user name ")  
#pas=input("pleas enter passsword ")
#user_pass(use,pas)
#if login(use, pas):
#    print("Welcome")
#else:
#    print("Invalid")\#
def add(a,b):
    return(a+b)
x=add(5,10)
print(x)        

def circle_area(radius):
    return (radius*radius*3.14)
answer= circle_area(5)
print(answer)

def max_number(a, b):
    if a>=b:
        return a
    else:
        return b
print(max_number(10, 5))
print(max_number(3, 8))
print(max_number(7, 7))    

def min_number(a,b):
    return min(a,b)
print(min_number(3,7))
def absolute(number):
    if number<0:
        return-number
    else:
        return number        
print(absolute(-5))

def is_positive(number):
    if number>=0:
        return True
    else:
        return False
print(is_positive(-0.2))
    