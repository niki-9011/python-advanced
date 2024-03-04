def triangle_func_forward(nums):
    figure = ""

    for n in range(1, nums + 1):
        for i in range(1, n + 1):
            figure += f"{i} "
        figure += "\n"

    for n in range(nums - 1, -1, -1):
        for i in range(1, n + 1):
            figure += f"{i} "
        figure += "\n"

    return figure

