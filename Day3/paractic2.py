#sen
Age=int(input('how old are you? '))
if Age in range(1,100):
    if Age<7:
        print("Kid")
    elif 7<=Age<18:
        print("Teenager")
    elif 18<=Age<60:
        print("Adult")
    elif 60<=Age:
        print("Senior")
else:
    print("alaki nagiiii?!")               