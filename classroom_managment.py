classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

def find_student_index(name):
    for index, student in enumerate(classroom):
        if student['name'] == name:
            return index
    return -1 


def add_student(name, email=None):
    if email is None:
        email = f"{name.lower()}@example.com"

    new_student = {
        'name': name,
        'email': email,
        'grades': []
    }

    classroom.append(new_student)



def delete_student(name):       
    del classroom[find_student_index(name)]
    



def set_email(name, email):
    if email is None:
        email[index]['email'] = email
    pass


def add_grade(name, profession, grade):
    index = find_student_index(name)
    if index != -1:
        classroom[index]['grades'].append((profession, grade))
   
    pass


def avg_grade(name, profession):
    
    sum,count=0,0
    index = find_student_index(name)       
    for prop, grade in classroom[index]['grades']:
        sum+=(grade)
        count += 1    
    return sum / count

    pass


def get_professions(name):
    index = find_student_index(name)
    l=[]
    for prop,_ in classroom[index]['grades']:
        if prop not in l:
            l.append(prop)

    return l
    
