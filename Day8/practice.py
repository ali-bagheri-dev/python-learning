student={
    'name':'ali',
    'age':'24',
    'city':'isfahan'
}
print(student['name'],'is',student['age'])
student['age']=25
print(student['age'])
student['job']=  'Programmer'
for key,value in student.items():
    print(key,':',value)

Amount=input('Enter your request: ')
if Amount in student :
    print(student[Amount])
else:
    print('not found') 
