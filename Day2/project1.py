name=input("what is your name? ")
Birth_year=int(input("when is your Birthyear? "))
if Birth_year in range(1926,2026):
    age=2026-Birth_year
    print(f'Hello {name.title()}')
    print(f' you are {age}')
    if age>= 18 :
        print("You are an adult.")
    else:
        print("You are under 18.")
else:
    print("Invalid birth year!")        