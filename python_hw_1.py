import math


a = 8
b = 10
c = 19
result_task_1 = a + b *(c / 2)
print ("Задача 1: Найти результат выражения "
       "для произвольных значений a,b,c: a + b *(c / 2)" 
       "Решение Задачи 1: Результат выражения для произвольных "
       "значений a,b,c: a + b *(c / 2), "
       "при значении а = %d, b = %d, c = %d,  "
       "равняется %d" % (a, b, c, result_task_1))


a = 89
b = 69
result_task_2 =(a**2 + b**2) % 2
print ("Задача 2: Найти результат выражения"
       "для произвольных значений a,b: (a2 + b2) %% 2"
       "Решение Задачи 2: Результат выражения для"
       "произвольных значений a,b: (a2 + b2) %% 2"
       "при значении a = %d и b = %d равняется %d" %
       (a, b, result_task_2))


a = 17
b = 21
c = 107
result_task_3 =(a + b) / 12 * c % 4 + b
print ("Задача 3: Найти результат выражения"
       "для произвольных значений a,b,c:(a + b) / 12 * c %% 4 + b"
       "Решение Задачи 3: Результат выражения для произвольных"
       "значений a,b,c:(a + b) / 12 * c %% 4 + b,"
      "при значении a = %d, b = %d, c = %d получаем"
       "%d" % (a, b, c, result_task_3))


a = 66
b = 99
c = 88
result_task_4 =(a - b * c) /(a + b) % c
print("Задача 4: Найти результат выражения для"
      "произвольных значений a,b,c:(a - b * c) /(a + b) %% c"
      "Решение Задачи 4: Результат выражения для произвольных"
      "значений a,b,c: ( a - b * c ) / ( a + b ) %% c"
      "при значении a = %d, b = %d, c = %d, получаем"
      "%d" % (a, b, c, result_task_4))


a = 8
b = 56
c = 32
result_task_5 = math.fabs(a - b) / (a + b)**3 - math.cos(c)
print("Задача 5: Найти результат выражения для произвольных"
      "значений a,b,c: | a - b | /(a + b)3 - cos(c)"
      "Решение Задачи 5: Результат выражения для произвольных"
      "значений a,b,c: | a - b | /(a + b)**3 - cos(c), "
      "при значении a = %d, b = %d, c = %d, получаем "
      "%d" % (a, b, c, result_task_5))


a = 26
b = 454
c = 23
result_task_6 =(math.log(1 + c) / -b)**4+ math.fabs(a)
print("Задача 5: Найти результат выражения для произвольных"
      "значений a,b,c: (ln( 1 + c ) / -b)4+ | a |"
      "Решение Задачи 6: Результат выражения для произвольных"
      "значений a,b,c: (ln(1 + c) / -b)**4+ | a |"
      "при значении a = %d, b = %d, c = %d, получаем "
      "%d" % (a, b, c, result_task_6))



