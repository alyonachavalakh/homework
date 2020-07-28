#Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
#Найти самого успешного и самого отстающего по среднему баллу.

students = {"Vasya": [5, 10, 10, 4, 5],
            "Petya": [4, 1, 10, 3, 5],
            "Sasha": [10, 10, 2, 4, 5],
            "Vanya": [5, 5, 10, 4, 5]}


def average_score(std):
    my_dict = {}
    for i in std.keys():
        my_dict[i] = sum(std[i])/len(std[i])
    return my_dict


def best_student(std):
    a = ('', 0)
    for name, score in std.items():
        if score > a[1]:
            a = name, score
    return a


def worst_student(std):
    a = ('', 11)
    for name, score in std.items():
        if score < a[1]:
            a = name, score
    return a


if __name__ == '__main__':
    print(average_score(students))
    print(best_student(average_score(students)))
    print(worst_student(average_score(students)))
