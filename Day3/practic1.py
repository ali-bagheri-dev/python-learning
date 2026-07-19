#nomre
Score=int(input('az 1 ta 100 chand midi? '))
if Score in range(1,101):
    if 90<=Score<=100:
        print("Excellent")
    elif 70<=Score<90:
        print("Good")
    elif 50<=Score<70:
        print("pass")
    else:
        print("Failed")
else:
    print("Invalid Score")               