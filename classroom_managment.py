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
index = find_student_index('Charlie')
print(index)
def add_student(name, email=None):
    if email is None:
        email = f"{name.lower()}@example.com"

    new_student = {
        'name': name,
        'email': email,
        'grades': []
    }

    classroom.append(new_student)

    pass


def delete_student(name):
    index = find_student_index(name)
    if index != -1:
        del classroom[index]
    pass



def set_email(name, email):
    index = find_student_index(name)
    if index != -1:
        email[index]['email'] = email
    pass


def add_grade(name, profession, grade):
    index = find_student_index(name)
    if index != -1:
        classroom[index]['grades'].append((profession, grade))
   
    pass


def avg_grade(name, profession):
    index = find_student_index(name)
    sum=count=0
    if index != -1:          
        for _, grade in student['grades']:
            sum+=(grade)
            count += 1
    average = sum(sum) / count
    return average

    pass


def get_professions(name):
    professions = set()

    for student in classroom:
        if student['name'] == name:
            for subject, _ in student['grades']:
                professions.add(subject)

    return list(professions)
    pass
