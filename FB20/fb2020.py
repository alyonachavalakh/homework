f = open('values1.txt')
numberlines = list()
for line in f.readlines():
        numberlines.extend(line.rstrip().split('/n')) #разделили файл на строки
digits = []
for item in numberlines:
    digits.extend(item.strip().split(' ')) #разделили строки на числа
    for x in range(0, len(digits), 3):
        a = int(digits[x])
    for y in range(1, len(digits), 3):
        b = int(digits[y])
    for z in range(2, len(digits), 3):
        c = int(digits[z])
    l = []
    for num in range(1, c + 1):
        if (num % a == 0) and (num % b == 0):
            print('FB')
        elif num % a == 0:
            print('F')
        elif num % b == 0:
            print('B')
        else:
            print(num)

with open('resultforfb20.py','w') as r:
    print([l], file=r)