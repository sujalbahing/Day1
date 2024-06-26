
me = {
    'name': 'Sujal',
    'address': 'dharan',
    'age': 18,
}

for x in me:
    print(x)


tuple = [0,2,"Apple",9]

# deleting the address

del me['age']

print(me)

print(me['name'])
print(me.keys())

mytuple = (1,3,5,6)
mytuple[0] = 'bob'



fruits = ['apple', 'orange', 'banana']

for x in fruits:
    print(x)



colors = ['red', 'green', 'orange']

for x in colors:
    print(x)
    
uni_num = [1,2,3,4,5]

for num in uni_num:
    print(num)


student_gardes = {
    'Sujal' : 89,
    'Nij' : 76,
    'Bib' : 32,
}

print(student_gardes.values())
print(student_gardes.items())

for x in student_gardes:
    print(x,"scored",student_gardes(x))
    
    
for student,gardes in student_gardes.items():
    print(x,"scored",gardes)
    
for value in student_gardes.values():
    print(value)
    
message = 'This much for today'

for char in message:
    print(char)


for x in range(1,52):
    print(x)