
print("Task 7: Преобразовать строку с американским форматом даты в европейский."
      "Например, '05.17.2016' преобразуется в '17.05.2016'")

american_date_format = "05.17.2016"
day = american_date_format[0:2]
month = american_date_format[3:5]
year = american_date_format[6:]

european_date_format = "{month}.{day}.{year}".format(day=day, month=month, year=year)
print(european_date_format)




print("Task 8: Дана строка с именем студента, в которой имя предшествует фамилии, например  ‘Mark Zuckerberg‘."
      "Написать программу, которая преобразует эту строку, ставя фамилию на первое место, а имя на второе."
      "Т.е. ‘Mark Zuckerberg‘ -> ‘Zuckerberg Mark‘.")

initial_name = "Mark Zuckerberg"
first_name = initial_name[0:4]
last_name = initial_name[5:]

converted_name = "{last_name} {first_name}".format(first_name=first_name, last_name=last_name)
print(converted_name)

# print("Task 9: Написать программу, которая преобразует имя переменной в формате snake_style в формат CamelizedStyle."
#       "Для простоты считаем, что имя переменной всегда состоит из 3-х слов."
#       "Например: ‘employee_first_name’ -> ‘EmployeeFirstName’")
# PS: Вот тут прям вообще застряла....


print("Task 10: Дана строка вида 'Leo Tolstoy*1828-08-28*1910-11-20'. "
      "В этой строке указаны имя писателя и через символ * даты рождения и смерти. "
      "Даты указаны в формате 'YYYY-MM-DD'. Требуется написать программу, "
      "которая по переданной строке определит возраст писателя и распечает его имя и возраст. "
      "Например, для строки 'Leo Tolstoy*1828-08-28*1910-11-20' программа должна распечатать: 'Leo Tolstoy, 82'. "
      "Для строки 'Marcus Aurelius*121-04-26*180-03-17' - 'Marcus Aurelius, 59'. "
      "Примечаение: Т.к. имена могут быть разной длины, то индексы символов разделителей ('*', '-') будут разными! "
      "Месяцы и дни можно игнорировать.")

graf_information = "Leo Tolstoy*1828-08-28*1910-11-20"
graf_information_split = graf_information.split('*')
graf_name = graf_information_split[0]
graf_birth_date = graf_information_split[1]
graf_death_date = graf_information_split[2]
birth_split = graf_birth_date.split("-")
death_split = graf_death_date.split("-")
birth_year = int(birth_split[0])
death_year = int(death_split[0])
age = death_year - birth_year
print("Graf’s name and age:")
print("%s , %d" % (graf_name, age))


emperor_information = "Marcus Aurelius*121-04-26*180-03-17"
emperor_information_split = emperor_information.split('*')
emperor_name = emperor_information_split[0]
emperor_birth_date = emperor_information_split[1]
emperor_death_date = emperor_information_split[2]
birth_split = emperor_birth_date.split("-")
death_split = emperor_death_date.split("-")
birth_year = int(birth_split[0])
death_year = int(death_split[0])
age = death_year - birth_year
print("Rome emperors name and age:")
print("%s , %d" % (emperor_name, age))