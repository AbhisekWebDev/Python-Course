phno = dict(
    {
    'Abhi':9000000000,
    'Nav':7000000000,
    'Kumar':9000000000,
    'Ram':3216549870
    }
)

print(phno['Abhi'])

phno['Abhi'] = 5000000000 # modifying the value in the dictionary, hence dictionary is mutable
print(phno)

phno['Mohan'] = {100000000, 2000000000} # adding list to the dictionary
print(phno)
print(phno['Mohan'])

phno['Shyam'] = {'Home':3000000000, 'Office':4000000000} # adding dictionary to the dictionary, hence nested dictionary
print(phno)
print(phno['Shyam'])
print(phno['Shyam']['Home'])

print(phno.get('Nav'))

del phno['Kumar']
print(phno)

print(phno.pop('Abhi'))

print(phno.popitem()) # popitem will remove the last item from the dictionary

print(phno.keys())

print(phno.values())

print(phno.items()) # items() will show the dictionary items in the form of tuples

for i in phno:
    print(i, phno[i])

for i in phno.items():
    print(i)






# NESTED DICTIONARY

student_data = dict(
    {
        'Ram':{'roll': 10, 'age': 20, 'course': 'Python'}
        ,
        'Mohan':{'roll': 20, 'age': 22, 'course': 'JS'}
    }
)

print(student_data)

print(student_data['Mohan'])

print(student_data['Ram']['age'])

student_data['Mohan']['phn_no'] = 951357820
print(student_data)







# NESTED LIST IN DICTIONARY

travel_data = dict(
    {
        'Gujrat':['dwarkadhish', 'somnath', 'unity']
        ,
        'Rajesthan':['jaipur', 'udaipur']
    }
)

print(travel_data)




# NESTED DICTIONARY IN LIST

data_students = [
    {'name': 'Ram', 'roll': 10, 'age': 20, 'course': 'Python'}
        ,
    {'name': 'Mohan', 'roll': 20, 'age': 22, 'course': 'JS'}
]

print(data_students)

print(data_students[1]['age'])




# looping through dictionary

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])