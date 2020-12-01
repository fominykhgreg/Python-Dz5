"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу,
открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""


f = open("text5.4.txt", encoding = "utf-8")
f1 = open("text5.4new.txt", "tw", encoding = "utf-8")
data = f.readlines()

i = 0
newWords = []
while i < len(data):
    newWords.append(data[i].split())
    i += 1

words = ["Один", "Два", "Три", "Четыре"]
j = 0
while j < len(data):
    f1.write(words[j]+" "+newWords[j][1]+" "+newWords[j][2]+"\n")
    j += 1

f.close()
f1.close()
