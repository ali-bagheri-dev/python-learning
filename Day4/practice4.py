number=int(input("jam 1 ta chad ro mikhay? "))
i=1
sum=0
j=[]
while i<=number:
    j.append(i)
    sum=i+sum
    i+=1   
print('+'.join(map(str,j)),'=',sum) 