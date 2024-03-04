number_students = int(input())

students = {}

for num in range(number_students):
    name, grade = input().split()
    if name not in students:
        students[name] = []
        students[name].append(float(grade))
    else:
        students[name].append(float(grade))

for student_name , student_grade in students.items():
    average_grade = sum(student_grade) / len(student_grade)
    grade_list = " ".join(str(f'{grade:.2f}') for grade in student_grade)

    print(f"{student_name} -> {grade_list} (avg: {average_grade:.2f})")
