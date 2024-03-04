def print_func(student_courses, result):
    data = []

    if result >= 240:
        data.append(f"Diyan gets a diploma with {result:.1f} credits.")

        for key, value in student_courses.items():
            data.append(f"{key} - {value:.1f}")

        return "\n".join(data)

    else:
        data.append(f"Diyan needs {240 - result:.1f} credits more for a diploma.")

        for key, value in student_courses.items():
            data.append(f"{key} - {value:.1f}")

        return "\n".join(data)


def students_credits(*args):
    student_courses = {}
    result = 0

    for x in args:
        course_name, credits, max_test_points, diyan_points = x.split("-")
        credit_course = (int(diyan_points) / int(max_test_points)) * int(credits)

        student_courses[course_name] = credit_course

    result = sum(student_courses.values())

    student_courses = dict(sorted(student_courses.items(), key=lambda x: -x[1]))
    output = print_func(student_courses, result)

    return output


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

#
# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )


# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )
