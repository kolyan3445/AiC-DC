#Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), распознает, преобразует и выводит на экран числа по определенному правилу. Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные выражения использовать нельзя.
#Натуральные числа, состоящие из цифр в порядке возрастания. Для каждого числа минимальную и максимальную цифру вывести прописью.

dict = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}


def num_to_text(number):
    return dict[number]  # словарь


buffer_size = 1
work_buffer = ''
numbers = []

with open("test1.txt", "r") as file:
    buffer = file.read(buffer_size)
    if not buffer:
        print("\nФайл пуст. Добавьте не пустой или переименуйте уже существующий *.txt файл.")
    while buffer:
        while buffer >= '0':
            if buffer >= '0':
                work_buffer += buffer
            buffer = file.read(buffer_size)
        if len(work_buffer) > 1:
            for i in range(len(work_buffer)):
                try:
                    if work_buffer[i] < work_buffer[i + 1]:
                        pass
                    else:
                        break
                except IndexError:
                    numbers.append(work_buffer)
                    break

        work_buffer = ''
        buffer = file.read(buffer_size)

for i in numbers:
    ans = 'min = ' + num_to_text(i[0]) + ', max = ' + num_to_text(i[len(i) - 1])
    print(i + ' - ' + ans)