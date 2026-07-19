fruits=["apple","banana","orange"]
print(fruits[0])
print(fruits[-1])
fruits.append("kiwi")
fruits.remove("banana")
print(fruits)
for fruit in fruits:
    print(fruit)
fruit_name=input("enter fruit name  ")
if fruit_name in fruits:
    print('found')
else:
    print("not found")    