import re
from constants import (SEPARATORS, NON_DECLARATIVE_SEPARATORS,
                       WORD, NUMBER,
                       ABBREVIATION, ABBREVIATION_TWO_WORDS)


def amount_of_sentences(str_):
    amount = len(re.findall(SEPARATORS, str_))

    for i in ABBREVIATION:
        amount -= str_.count(i)

    for i in ABBREVIATION_TWO_WORDS:
        amount -= str_.count(i) * 2

    return amount


def amount_of_non_declarative_sentences(str_):
    amount = len(re.findall(NON_DECLARATIVE_SEPARATORS, str_))

    return amount


def average_length_of_the_sentences(str_):
    numbers = re.findall(NUMBER, str_)
    words_re = re.findall(WORD, str_)
    words = []
    for i in words_re:
        if i not in numbers:
            words.append(i)
    sentence_len_in_characters = 0
    for i in words:
        sentence_len_in_characters += len(i)

    amount = amount_of_sentences(str_)

    average_length_sentences = sentence_len_in_characters / amount
    return average_length_sentences


def average_length_of_the_world(str_):
    numbers = re.findall(NUMBER, str_)
    words_re = re.findall(WORD, str_)
    words = []

    for i in words_re:
        if i not in numbers:
            words.append(i)
    sentence_len_in_characters = 0

    for i in words:
        sentence_len_in_characters += len(i)
    words_len = len(words)
    average_length_words = sentence_len_in_characters / words_len

    return average_length_words


