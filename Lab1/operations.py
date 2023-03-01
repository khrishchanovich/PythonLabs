from constants import ALLOWED_OPERATIONS


def func_operation(a, b, operation):
    result = 0

    if operation == ALLOWED_OPERATIONS[0]:
        result = a + b
    if operation == ALLOWED_OPERATIONS[1]:
        result = a - b
    if operation == ALLOWED_OPERATIONS[2]:
        result = a * b
    if operation == ALLOWED_OPERATIONS[3]:
        result = a / b

    return print(result)