def func1(str_):
    separators = ['.', '?', '!']
    counter = 0
    str_split = []
    for i in range(len(str_)):
        if str_[i] in separators:
            str_split.append(str_[counter:i+1])
            counter = i + 1
    return map(lambda s: str_.strip(), str_split)
