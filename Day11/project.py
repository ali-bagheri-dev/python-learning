import calculator
import validation

while True:
    number1=validation.get_number1
    number2=validation.get_number2
    Operation=input('which one? *,/,+,-,exit: ')
    
    if Operation=="+":
        print(calculator.add(number1,number2))
    elif Operation=="-":
        print(calculator.sub(number1,number2))
    elif Operation=="*":
        print(calculator.mult(number1,number2))
    elif Operation=="/":
        try:
            print(calculator.div(number1,number2))
        except ZeroDivisionError:
            print("You cannot divide by zero.")    
    elif Operation=='exit':
        break