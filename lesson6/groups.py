# Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java).
# Студент может учиться в нескольких группах. Затем вывести:
# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java

students = {"Vasya": ["Java"],
            "Petya": ["Python", "FrontEnd", "FullStack"],
            "Sasha": ["Python", "FullStack", "Java"],
            "Vanya": ["FrontEnd", "Java"]}


def two_and_more(std):
    res = {}
    for name, groups in std.items():
        if len(groups) >= 2:
            res[name] = groups
    return res


def no_front(std):
    res = {}
    for name, groups in std.items():
        if "FrontEnd" not in groups:
            res[name] = groups
    return res


def python_java(std):
    res = {}
    for name, groups in std.items():
        if "Python" in groups or "Java" in groups:
            res[name] = groups
    return res


if __name__ == '__main__':
    print(two_and_more(students))
    print(no_front(students))
    print(python_java(students))
