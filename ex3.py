# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет 
# с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


import os
def clear_console():
  os.system('cls')
clear_console()


print ("Проверка билета онлайн, без регистрации: ")
n = str(input())
if len(n) <=5:
   print("Ошибка")
else:
    arr = [int(x) for x in str(n)]
    first = arr[0]+arr[1]+arr[2]
    second = arr[3]+arr[4]+arr[5]
    if first==second:
        print(f'Билет можно есть -> {first} = {second}')
    else:
        print("Не сегодня :(")





# num = 2019
# print("The original number is " + str(num))
# res = [int(x) for x in str(num)]
# print("The list from number is " + str(res))




# print(f'list[{0},{1},{2}]')