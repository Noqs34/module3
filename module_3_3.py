def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [True, 'Strong', 34]
values_dict = {'a': False, 'b': 13, 'c': 'Winner'}
values_list_2 = [60, 'Disconnect']
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, True)