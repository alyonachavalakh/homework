#Вам известен номер квартиры, этажность дома и количество квартир на этаже.
#Задача: написать функцию, которая по заданным параметрам напишет вам,
#в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.

yourflat = {'flat number': int(input('enter the flat number: ')),
            'stairs': int(input('enter the quantity of stairs: ')),
            'flats on a stair': int(input('enter the quantity of flats on a stair: '))}


def find_flat(str):
    import math
    qflats = 0
    yourflatporch = 0
    yourflatstair = 0
    for i in str.values():
        i = str['stairs'] * str['flats on a stair']
        qflats = i
    for a in str.values():
        a = math.ceil(str['flat number'] / qflats)
        yourflatporch = a
    for b in str.values():
        if yourflatporch == 1 and str['flat number'] / str['flats on a stair'] < 1:
            yourflatstair = 1
        elif yourflatporch == 1 and str['flat number'] / str['flats on a stair'] > 1:
                yourflatstair = math.ceil(str['flat number'] / str['flats on a stair'])
        elif yourflatporch > 1:
            b = str['flat number'] - (yourflatporch - 1) * qflats
            yourflatstair = math.ceil(b / str['flats on a stair'])
    return yourflatporch, yourflatstair

print(('Your flat porch and stair are: '), find_flat(yourflat))
