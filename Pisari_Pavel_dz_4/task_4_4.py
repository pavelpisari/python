# Task4
"""*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве
аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи —
первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания
и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
 thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
"Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}

Как поступить, если потребуется сортировка по ключам?
"""


def thesaurus_adv(*names_surnames):
    out_dict = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        out_dict.setdefault(surname[0], {})
        out_dict[surname[0]].setdefault(name[0], [])
        out_dict[surname[0]][name[0]].append(name_surname)

    # sort example
    sorted_dict = {x: out_dict[x] for x in sorted(out_dict)}  # Dict Comprehensions
    return out_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
                    "Анна Савельева"))