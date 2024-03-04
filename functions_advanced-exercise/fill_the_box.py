def fill_the_box(height, length, width, *n_cubes):
    cube = height * length * width
    sum_cubes = 0

    for x in n_cubes:
        if x == "Finish":
            break
        else:
            sum_cubes += int(x)

    result = cube - sum_cubes

    if result > 0:
        return f"There is free space in the box. You could put {result} more cubes."
    else:
        return f"No more free space! You have {abs(result)} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
