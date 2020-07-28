#Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла! (без циклов не сложилось :((( )

import re
text = open('text.txt', 'r')
text_string = text.read().lower()
matching_words = re.findall(r'\b[a-z]{3,15}\b', text_string)
frequency = {}

for word in matching_words:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
for words in frequency_list:
    print(words, frequency[words])