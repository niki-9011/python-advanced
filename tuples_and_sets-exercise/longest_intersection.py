def print_func(result):
    max_len = 0
    max_list = []
    for z in result:
        if len(z) > max_len:
            max_len = len(z)
            max_list = z

    print(f"Longest intersection is {[x for x in max_list]} with length {max_len}")

def longest_intersection(n):
    result = []
    set_first = set()
    set_second = set()
    for x in range(n):
        first_index, second_index = input().split("-")

        first = [int(x) for x in first_index.split(",")]
        second = [int(j) for j in second_index.split(",")]

        first_start = first[0]
        first_stop = first[1]
        second_start = second[0]
        second_stop = second[1]

        [set_first.add(j) for j in range(first_start, first_stop + 1)]
        [set_second.add(k) for k in range(second_start, second_stop + 1)]

        result.append(set_first.intersection(set_second))
        set_first.clear()
        set_second.clear()

    print_func(result)

n = int(input())
longest_intersection(n)
