def print_params(a=1, b='строка', c=True):

  print(a, b, c)

print_params()
print_params(10)
print_params(10, 'Текст')
print_params(10, 'Текст', False)

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, 'Другая строка', False]
values_dict = {'a': 5, 'b': 'Ещё одна строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)