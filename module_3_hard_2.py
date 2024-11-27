def calculate_structure_sum(struct):
    total = 0
    for arg in struct:
        if isinstance(arg,(float, int)):
            total += arg
        elif isinstance(arg, str):
            total += len(arg)
        elif isinstance(arg, (list, tuple, set)):
            total += calculate_structure_sum(arg)
        elif isinstance(arg, dict):
            for i in arg.items():
                for j in i:
                    if isinstance(j, str):
                        total += len(j)
                    elif isinstance(j , (int, float)):
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