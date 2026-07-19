number=int(input("chanta danesh amoz dari? "))
i=1
sum=0

while i<=number:
    print(f'nomre dansh amoz{i}')
    i+=1
    count=int(input())
    if 0<=count<=20:
        sum+=count
    else:
        print("az aval bezan")
        break         

average=sum//number
if 17<average<=20:
    print(f'average is {average} excellent')
elif 12<=average<=17:   
    print(f'average is {average} good')
else:
    print(f'average is {average} Need Improvement')
    
