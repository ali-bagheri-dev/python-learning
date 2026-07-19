
with open('hello.txt','w') as file:
    file.write('hello ali')
with open('hello.txt','a') as file:
    file.write('\nToday is Day9\n')
name=input('enter your nam: ')    
with open('hello.txt','a') as file:
    file.write('\n'+name)
with open('hello.txt','r') as file:
    text=file.read()
print(text)    