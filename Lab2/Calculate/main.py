import re
from constants import SEPARATORS, NON_DECLARATIVE_SEPARATORS
str_ = "Hello! How are you? I'm fine. Thank you... I love you!"

len_all = len(re.findall(SEPARATORS, str_))

print(len_all)

len_non_declarative = len(re.findall(NON_DECLARATIVE_SEPARATORS, str_))

print(len_non_declarative)


