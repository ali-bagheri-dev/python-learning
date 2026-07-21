def mult(number1,number2):
    return number1*number2

def add(number1,number2):
    return number2+number1
    
def sub(number1,number2):
    return  number1-number2
    
def div(number1,number2):
    return number1//number2     

while True:
    while True:
        try:
            number1=int(input('enter number 1: '))
            break
        except ValueError:
            print('invalid number')
        
    while True:
        try:
            number2=int(input('enter number 2: '))
            break
        except ValueError:
            print('invalid number')
    Operation=input('which one? *,/,+,-,exit: ')
    
    if Operation=="+":
        answer=add(number1,number2)
        print(answer)
    elif Operation=="-":
        answer=sub(number1,number2)
        print(answer)
    elif Operation=="*":
        answer=mult(number1,number2)
        print(answer)
    elif Operation=="/":
        try:
            answer=div(number1,number2)
            print(answer)
        except ZeroDivisionError:
            print("You cannot divide by zero.")    
    elif Operation=='exit':
        break

