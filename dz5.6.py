"""Необходимо создать (не программно) текстовый файл,
 где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

f = open("text5.6.txt", encoding = "utf-8")
a = f.readlines()

"""Находим числа в строках"""
count = 0
num_list = []
peremen = []
while count < len(a):
    b = a[count]
    count += 1

    num = ''
    for char in b:
        if char.isdigit():
            num = num+char
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))
    ex = sum(num_list)
    peremen.append(ex)
    num_list = []

print(peremen)

"""Находим названия предметов"""
i = 0
newData = []
while i < len(a):
    c = a[i].split()
    newData.append(c)
    i += 1

newLessons = []
j = 0
while j < len(newData):
    newLessons.append(newData[j][0])
    j += 1
print(newLessons)

"""Заполняем готовый словарь"""
gotov = {}
k = 0
while k < len(newLessons):
    gotov[newLessons[k]] = peremen[k]
    k += 1
print(gotov)

f.close()
