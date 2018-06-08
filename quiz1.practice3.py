students = [
    {   
        "name": "Kim",
        "kor": 80,
        "eng": 90,
        "math": 80
    },
    {   
        "name": "Lee",
        "kor": 90,
        "eng": 85,
        "math": 85
    }
]

for student in students:
    total = student.get('kor')+student.get('eng')+student.get('math')
    avg = total / 3
    student['total'] = total
    student['avg'] = avg

#total = (students.values())
#d = dict(total = students[0]['kor']+students[0]['eng']+students[0]['math']+
#    students[1]['kor']+students[1]['eng']+students[1]['math']
#, avg = students[0]['kor']+students[0]['eng']+students[0]['math']+
#students[1]['kor']+students[1]['eng']+students[1]['math'] / 6)

# print(d)
print(students)

