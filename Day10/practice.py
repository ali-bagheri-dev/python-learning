def mult(number1,number2):
    mult=number1*number2
    return mult
def sum(number1,number2):
    sum=number2+number1
    return sum
def sub(number1,number2):
    sub= number1-number2
    return sub
def div(number1,number2):
    div=number1//number2
    return div
answer=0
while True:
    while True:
        try:
            number1=int(input('enter number 1: '))
            break
        except ValueError:
            print('invalid number')
        
            
    try:
        number2=int(input('enter number 2: '))
    except ValueError:
        print('invalid number')
        break
    Operation=input('which one? *,/,+,-,exit: ')

    if Operation=="+":
        answer=sum(number1,number2)
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
    print('invalid')
