# Python_Hub_Studio
# Python_7_Hours

# ЦИКЛ while

'''
БЕСКОНЕЧНЫЙ ЦИКЛ
while True:
	print("True")
'''


x = 0 # переменная-счетчик

while x < 5:
	x +=1
	print(x)
else:
	print("x > 5 Завершение цикла")


# ФАКТОРИАЛ ЧИСЛА

while True:
	x = int(input("Введите число: "))
	assert x >= 0, "Факториал отрицательного не определен"
	count = 0
	y = 1

	while count < x:
		count +=1
		y *= count
	else:
		print("Факториал числа " + str(x) + " равен " +str(y))


# ЦИКЛ while

# напишем слово из 5 букв
x = ""
max_len = int(input("Из скольки букв состоит слово? ")) # максимальная длина слова (максимумальное кол-во букв в слове)

while len(x) < max_len:
	# можно вводить буквы последовательно, а можно написать слово сразу, игнорируя 'continue'
	y = input("Ввод данных: ")
	# переводим буквы в слове в нижний регистр
	y = y.lower()
	# создаем условие, при котором к слову "x" не добавляется буква "l"
	if y == "l":
		# буква не добавляется к слову и цикл вызывается заново
		print("Слово не может содержать букву 'l'. Повторите ввод.")
		continue
	# создаем условие, при котором происходит выход из цикла
	if y == "o":
		# при вводе буквы "o" цикл прерывается
		print("Вы ввели букву 'o'. Программа прервана.")
		break
	x += y # добавляем текст к строке
else:
	print("Ввод успешно завершен.")
	print("Слово из " + str(max_len) + " букв: " + x)
