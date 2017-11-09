import math

#________________________________
#Print Rectungle Squire
#height = 10
#width = 20
#rectangle_squire = height * width
#print ("Rectangle squire due to height %d and width %d is %d sq.sm." % (height, width, rectangle_squire))

#______________________________
#Print Circule squire
#radius = 42
#circule_squire = radius**2 * math.pi
#print ("Circule squire due to radius %d is %.2f" % (radius, circule_squire))


#______________________________
#print ("Юникодный символ с кодом %d выглядит %s" % (0x26BD, "\u26BD"))

#print ("Юникодный символ с кодом %d выглядит %s" % (0x1F5FC, "\U0001F5FC"))

#print ("Юникодный символ с кодом %d выглядит %s" % (0x1F43F, "\U0001F43F"))

#print ("Юникодный символ с кодом %d выглядит %s" % (0x221E, "\U0000221E"))

#print ("Юникодный символ с кодом %d выглядит %s" % (0x1F608, "\U0001F608"))


#______________________________
                #01234567
#current_time = "18:38:01"
#hours = int (current_time [0:2])
#print (hours)
#print (type(hours))
#minutes = int (current_time [3:5])
#print (minutes)
#seconds = int (current_time [6:])
#print (seconds)
#total_seconds = hours*3600 + minutes*60 + seconds
#print (total_seconds)
#total_seconds = hours*3600 + minutes*60 + seconds


#______________________________

#current_time = "8:8:1"
#current_time.split(" : ")
#print (current_time.split (" : "))
#lst = current_time
#print (lst [0])
#print (lst [1])
#print (lst [2])
#print (lst [3])
#print (lst [4])
#print (list)

#current_time = "8:8:1"
#lst = current_time.split (":")
#hours = int (lst [0])
#hours = int (lst [1])
#hours = int (lst [2])
#print (hours, minutes, seconds)
#total_seconds = hours*3600 + minutes*60 + seconds
#print (total_seconds)

#________________________________________________________________________________________________________________________


a = 8
b = 10
c = 19
result_task_1 = a + b * ( c / 2 )
print ("Задача 1: Найти результат выражения для произвольных значений a,b,c: a + b * ( c / 2 )"
    "\nРешение Задачи 1: Результат выражения для произвольных значений a,b,c: a + b * ( c / 2 ), "
       "при значении а = %d, b = %d, c = %d,  равняется %d" % (a, b, c, result_task_1))


#_____________________________

a = 89
b = 69
result_task_2 = ( a**2 + b**2 ) % 2
print ("Задача 2: Найти результат выражения для произвольных значений a,b: (a2 + b2) %% 2 "
       "\nРешение Задачи 2: Результат выражения для произвольных значений a,b: ( a2 + b2 ) %% 2"
       "при значении a = %d и b = %d равняется %d" % (a, b, result_task_2))


#_____________________________

a = 17
b = 21
c = 107
result_task_3 = ( a + b ) / 12 * c % 4 + b
print ("Задача 3: Найти результат выражения для произвольных значений a,b,c: ( a + b ) / 12 * c %% 4 + b "
       "\nРешение Задачи 3: Результат выражения для произвольных значений a,b,c: ( a + b ) / 12 * c %% 4 + b, "
      "при значении a = %d, b = %d, c = %d получаем %d" % (a, b, c, result_task_3))



#_____________________________

a = 66
b = 99
c = 88
result_task_4 = ( a - b * c ) / ( a + b ) % c
print("Задача 4: Найти результат выражения для произвольных значений a,b,c: (a - b * c ) / ( a + b ) %% c "
      "\nРешение Задачи 4: Результат выражения для произвольных значений a,b,c: ( a - b * c ) / ( a + b ) %% c, "
      "при значении a = %d, b = %d, c = %d, получаем %d" % (a, b, c, result_task_4))


#_____________________________

a = 8
b = 56
c = 32
result_task_5 = ( a - b )**3 / ( a + b )**3 - math.cos( c )
print("Задача 5: Найти результат выражения для произвольных значений a,b,c: | a - b | /( a + b)3 - cos( c )"
      "\nРешение Задачи 5: Результат выражения для произвольных значений a,b,c: | a - b | /( a + b)**3 - cos( c ), "
      "при значении a = %d, b = %d, c = %d, получаем %d" % (a, b, c, result_task_5))


#_____________________________
a = 26
b = 454
c = 23
result_task_6 = ( math.log( 1 + c ) / -b )**4+ a**3
print("Задача 5: Найти результат выражения для произвольных значений a,b,c: ( ln( 1 + c ) / -b )4+ | a | "
      "\nРешение Задачи 6: Результат выражения для произвольных значений a,b,c: ( ln( 1 + c ) / -b )**4+ | a |, "
      "при значении a = %d, b = %d, c = %d, получаем %d" % (a, b, c, result_task_6))




