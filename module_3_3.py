#1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(2, 8, 'hello')
print_params(100)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

#2
values_list = [3, 'cat', False]
values_dict = {'a' : 10, 'b' : True, 'c' : 'dog'}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = ['word', 15]
print_params(*values_list_2, 42)
