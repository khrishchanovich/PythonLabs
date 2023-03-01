from helloworld import hello_world
from operations import func_operation
from listofnumbers import list_numbers

print('---1---')
hello_world()

print('---2---')
a = int(input('first val: '))
b = int(input('second val: '))
operation = input('operation (add, sub, mult, div): ')
func_operation(a, b, operation)

print('---3---')
list_numbers()