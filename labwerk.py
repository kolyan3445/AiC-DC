#Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), распознает, преобразует и выводит на экран числа по определенному правилу. Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные выражения использовать нельзя.
#Натуральные числа, состоящие из цифр в порядке возрастания. Для каждого числа минимальную и максимальную цифру вывести прописью.

word_dict = {
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять',
    '0': 'ноль'
}

# Открытие файла
filename = 'test1.txt'
block_size = 100

with open(filename, 'r') as f:
    # Поблочное чтение из файла
    while True:
        block = f.read(block_size)
        if not block:
            break

        # Разбитие блока
        chars = list(str(block.split()))
        i = 0
        while i < len(chars):
            # Проверка на число
            if chars[i].isnumeric():
                num_str = chars[i]
                i += 1
                while i < len(chars) and chars[i].isnumeric():
                    num_str += chars[i]
                    i += 1
                # Проверка на возрастание
                is_ascending = True
                for j in range(len(num_str) - 1):
                    if int(num_str[j]) >= int(num_str[j + 1]):
                        is_ascending = False

                # Перевод в слова
                if is_ascending:
                    min_digit = word_dict[min(num_str)]
                    max_digit = word_dict[max(num_str)]
                    print(num_str + ': ' + min_digit + ', ' + max_digit)

            else:
                i += 1