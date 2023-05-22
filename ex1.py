# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

import os

def clear_console():
  os.system('cls')

clear_console()


print ("Введите число: ")
n = str(input())
sum = 0
for el in n:
    sum = sum + int(el)
print (f'Сумма цифр числа {n} = {sum}')








