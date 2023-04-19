def serialize(data, tag):
    item = '<' + tag + '>'
    for key, value in data.items():
        if isinstance(value, dict):
            item += serialize(key, value)
        else:
            item += '<' + key + '>' + str(value) + '</' + key + '>'
    item += '</' + tag + '>'

    return item

