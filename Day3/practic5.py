#mashin hesab
Number1=int(input("Enter number1 "))
operaitor=input("Enter * or + or - or / ")
Number2=int(input("Enter number2 "))
answer=int(0)
if operaitor=='*':
    answer=Number1*Number2
    print(answer)
elif operaitor=='+':
    answer=Number1+Number2
    print(answer)
elif operaitor=='-':
    answer=Number1-Number2
    print(answer)
elif operaitor=='/':
    answer=Number1/Number2
    print(answer)
else:
    print("Invalid operator")        