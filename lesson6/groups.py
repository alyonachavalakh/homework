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
