def softuni_students(*args, **kwargs):
    students = {}
    output_valid = []
    output_invalid = []

    for student_id, username in args:
        students[username] = student_id

    for student in sorted(students):
        if students[student] in kwargs:
            output_valid.append(f'*** A student with the username {student} has successfully finished the course {kwargs[students[student]]}!')
        else:
            output_invalid.append(student)

    if not output_invalid:
        return '\n'.join(output_valid)
    else:
        return '\n'.join(output_valid) + '\n' + f'!!! Invalid course students: {", ".join(output_invalid)}'

# print(softuni_students(
#     ('id_1', 'Kaloyan9905'),
#     id_1='Python Web Framework',
# ))
#
# print(softuni_students(
#     ('id_7', 'Silvester1'),
#     ('id_32', 'Katq21'),
#     ('id_7', 'The programmer'),
#     id_76='Spring Fundamentals',
#     id_7='Spring Advanced',
# ))

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))