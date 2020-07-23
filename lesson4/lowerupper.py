def lower_case(string):
    return string.lower()


def upper_case(string):
    return string.upper()


strings = ['ReD', 'YelLow', 'BlACk', 'WhiTe', 'GrEEn']

new_list = list(map(lower_case, strings))
new_list1 = list(map(upper_case, strings))

print(new_list)
print(new_list1)
