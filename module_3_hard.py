def calculate_structure_sum(struct):
    total = 0
    for arg in struct:
        if type(arg) in (float, str, int):
            if type(arg) == str:
                total += len(arg)
            elif type(arg) == int or type(arg) == float:
                total += arg
        elif type(arg) in (list, tuple, set):
            total += calculate_structure_sum(arg)
        elif type(arg) in {dict}:
            for i in arg.items():
                for j in i:
                    if type(j) == str:
                        total += len(j)
                    elif type(j) == int or type(j) == float:
                        total += j
    return total
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)