import re
from constants import SEPARATORS, NON_DECLARATIVE_SEPARATORS, WORD, NUMBER
str_ = "Hello! How are you? I'm fine. Thank you... I love you! 5gd7 55"

len_all = len(re.findall(SEPARATORS, str_))

print(len_all)

len_non_declarative = len(re.findall(NON_DECLARATIVE_SEPARATORS, str_))

print(len_non_declarative)

print(str_)
numbers = re.findall(NUMBER, str_)
words_re = re.findall(WORD, str_)
words = []
for i in words_re:
    if i not in numbers:
        words.append(i)
sentence_len_in_characters = 0
for i in words:
    sentence_len_in_characters += len(i)
print(sentence_len_in_characters)
average_length_sentences = sentence_len_in_characters / len_all
print(average_length_sentences)

words_len = len(words)
print(words_len)

average_length_words = sentence_len_in_characters / words_len
print(average_length_words)

