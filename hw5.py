# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
# У пользователя необходимо запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, 
# то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print('Имеющиеся числа ' + str(my_list))
inp = int(input('Введите число '))

for i in range(len(my_list)):
    if my_list[i] == inp:
        my_list.insert(i + 1, inp)
    elif my_list[0] < inp:
            my_list.insert(0, inp)
    elif my_list[-1] > inp:
            my_list.append(inp)
    elif my_list[i] > inp and my_list[i + 1] < inp:
            my_list.insert(i + 1, inp)
    print('Имеющиеся числа ' + str(my_list))
    inp = int(input('Введите число '))


