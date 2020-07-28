#Написать 2 функции. Первая функция будет принимать строку и приводить ее к нижнему регистру.
#Вторая функция будет принимать строку и проводить ее к верхнему регистру.
#После чего с помощью map применить ваши функции к списку строк. Отдельно каждую функцию к отдельному списку строк!

def lower_case(string):
    return string.lower()


def upper_case(string):
    return string.upper()


strings = ['RED', 'YElLOW', 'BlACK', 'WHITE', 'GREEN']
strings1 = ['red', 'yellow', 'black', 'white', 'green']

new_list = list(map(lower_case, strings))
new_list1 = list(map(upper_case, strings1))

print(new_list)
print(new_list1)
