import string

str_ = input()
counter = 0
list_ = list(str_)
print(str_)
print(list_)

if list_[-1] == '.' or list_[-1] == '?' or list_[-1] == '...' or list_[-1] == '!':
    counter += 1

for i in range(len(list_)):
    if list_[i] == '.' and list_[i-1] == '.':
        a = str_.count('... ')
    if list_[i] == '.' and list_[i-1] == str_.isalpha():
        b = str_.count('. ')

