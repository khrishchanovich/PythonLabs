from function import amount_of_sentences, \
    amount_of_non_declarative_sentences, \
    average_length_of_the_sentences, \
    average_length_of_the_world

str_ = input('Enter text: ')

script1 = amount_of_sentences(str_)
script2 = amount_of_non_declarative_sentences(str_)
script3 = average_length_of_the_sentences(str_)
script4 = average_length_of_the_world(str_)
# script 5

print('Amount of sentences: ', script1,
      '\nAmount of non-declarative sentences: ', script2,
      '\nAverage length of the sentences in characters: ', script3,
      '\nAverage length of the world in the text in characters: ', script4)
