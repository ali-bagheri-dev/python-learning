def get_number1():
    while True:
        try:
            number= int(input('enter number 1: '))
            return number
            break
        except ValueError:
            print('invalid number')
def get_number2():        
    while True:
        try:    
            return int(input('enter number 2: '))
            break
        except ValueError:
            print('invalid number')