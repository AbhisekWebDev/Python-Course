student_data = [
    {
        'name': 'Ram', 
        'roll': 10, 
        'age': 20, 
        'course': 'Python'
        }
        ,
    {
        'name': 'Mohan', 
        'roll': 20, 
        'age': 22, 
        'course': 'JS'
        }
]

def add_new_student(n_name, n_roll, n_age, n_course):
    
    new_student = {}
    
    new_student['name'] = n_name
    new_student['roll'] = n_roll
    new_student['age'] = n_age
    new_student['course'] = n_course

    student_data.append(new_student)

add_new_student('Shyam', 22, 18, 'C')

print(student_data)