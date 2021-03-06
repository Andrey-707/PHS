# Python_Hub_Studio
# Python_7_Hours

# МНОЖЕСТВА. Практическое применение.

# Множества создаются при помощь встроенной функции set(). В неё передается итерируемая
# последовательность список, кортеж, строка или при помощи литерала фигурные скобки {}

# !!! МНОЖЕСТВА МОГУТ СОСТОЯТЬ ТОЛЬКО ИЗ НЕИЗМЕНЯЕМЫХ ТИПОВ ДАННЫХ, ТАКИХ КАК ЧИСЛО,
# КОРТЕЖ, СТРОКА !!!

t = {"строка_текста", "другая_строка_текста", 1, 2, 3, (3, 4, 5)}
y = set()
print(t) # OUT: {1, 2, 3, 'строка_текста', 'другая_строка_текста', (3, 4, 5)}

# Можно заметить, что после вывод эдементы перемешались. Это говорит о том, что во
# множествах отсутствуют индексы или какая-либо другая упорядоченность.

# Если множество содержитповторяющиеся элементы, то выводиться на экран они не будут
t = {"строка_текста", "строка_текста", 1, 2, 3, (3, 4, 5)}
y = set()
print(t) # OUT: {1, 2, 3, (3, 4, 5), 'строка_текста'}

# СУТЬ МНОЖЕСТВ.

x = (1, 2, 3, 4, 5, 6, 7) # кортеж
y = [1, 2, 3, 4, 5, 6, 7] # список
u = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7} # словарь
h = {1, 2, 3, 4, 5, 6, 7} # множество

# сколько оперативной памяти выделено: 
print(x.__sizeof__()) # OUT: 80
print(y.__sizeof__()) # OUT: 96 
print(u.__sizeof__()) # OUT: 344
print(h.__sizeof__()) # OUT: 712 # множества самые ресурсоемкие!!!

# ПРИМЕР ФУНКЦИИ ИЗ УРОКА №13
# Создадим функцию-алгоритм, которая принимает в качетсве аргументов списки и добавляет
# их элементы в новый список. При этом повторяющиеся значения отсеиваются.
# Импортируем модуль времени, чтобы проверить сколько времени потрубуется на 
# выполнение данной работы.

import time


def exclusive_item(*args):
	# список эксклюзивных элементов
	new_list = []
	# переменная-счетчик
	# фиксирует повторение элемента
	count = 0
	# итерация по переменной i (в нашем случае по спискам\кортежам)
	for i in args:
		# итерация по переменной j (в нашем случае по элементам\кортежам списка i)
		for j in i:
			# условие: если переменная j (элемент j списка\кортежа i) не в списке new_list
			if j not in new_list:
				# при сробатывании условия добавляет переменную j (элемент списка\кортежа)
				# в список new_list
				new_list.append(j)
			else:
				# Элемент повторяется, переменная-счетчик увеличена на +1
				count += 1
	print("Обнаружено повторений:", count)
	# возвращает список эксклюзивных элементов
	return new_list

list_1 = list(range(1000))
list_2 = list(range(500, 1500))
list_3 = list(range(1000, 2000))

# начало выполнения. Первое
start1 = time.time()

exclusive_item(list_1, list_2, list_3)

# затраченное время. Первое
stop1 = time.time() - start1
# OUT: Обнаружено повторений: 1000
#      0.04900002479553223
print(stop1)

# !!! Использование множества сокращает время выполнения !!!
# начало выполнения. Второе
start2 = time.time()
r = set(list_1) # превращение списка во множество
t = r.union(set(list_2), set(list_3)) # объединение множества из списков

exclusive_item(list_1, list_2, list_3)

# затраченное время. Второе
stop2 = time.time() - start2
# OUT: Обнаружено повторений 1000
#      0.03900027275085449
print(stop2)


# МЕТОДЫ МНОЖЕСТВ.

z = {1, 2, 3, 4, 5} # множество 1
x = {3, 4, 5, 6, 7} # множество 2

print(z) # OUT: {1, 2, 3, 4, 5}
print(type(z)) # OUT: <class 'set'>

# Метод .add() позволяет добавить элемент во множество.
z = {1, 2, 3, 4, 5} # множество 1
print(z) # OUT: {1, 2, 3, 4, 5}
z.add(6)
print(z) # OUT: {1, 2, 3, 4, 5, 6}

# Метод .add() НЕ МОЖЕТ добавлять одинаковые элементы во множества.
z = {1, 2, 3, 4, 5} # множество 1
print(z) # OUT: {1, 2, 3, 4, 5}
z.add(3)
print(z) # OUT: {1, 2, 3, 4, 5}

# Метод .discard() позволяет удалить элемент из множества. Если элемента нет во
# множестве, то при попытке его удаления не возникает ошибки.
z = {1, 2, 3, 4, 5} # множество 1
print(z) # OUT: {1, 2, 3, 4, 5}
z.discard(5)
print(z) # OUT: {1, 2, 3, 4}

# Метод .remove() позволяет удалить элемент из множества.
z = {1, 2, 3, 4, 5} # множество 1
print(z) # OUT: {1, 2, 3, 4, 5}
z.remove(5)
print(z) # OUT: {1, 2, 3, 4}

# Метод .remove() приводит к ошибке, если множество не содержит элемент.
z = {1, 2, 3, 4, 5} # множество 1
print(z) # OUT: {1, 2, 3, 4, 5}
z.remove(6)
print(z) # OUT: KeyError: 6

# Метод .union() позволяет обьединить множества. При этом необходимо сохранить в
# новую переменную. Не будет содержать повторяющиеся элементы.
z = {1, 2, 3, 4, 5} # множество 1
x = {3, 4, 5, 6, 7} # множество 2
print(z) # OUT: {1, 2, 3, 4, 5}
print(x) # OUT: {3, 4, 5, 6, 7}
y = z.union(x) # другая запись: "set | other_set"
print(y) # OUT: {1, 2, 3, 4, 5, 6, 7}

# Метод .update() позволяет обьединить множества. Без сохранения в переменную.
# Не будет содержать повторяющиеся элементы.
z = {1, 2, 3, 4, 5} # множество 1
x = {3, 4, 5, 6, 7} # множество 2
print(z) # OUT: {1, 2, 3, 4, 5}
print(x) # OUT: {3, 4, 5, 6, 7}
z.update(x) # другая запись: "set |= other_set"
print(z) # OUT: {1, 2, 3, 4, 5, 6, 7}

# Метод .difference() позволяет определить разницу между множествами, т.е. позволяет
# определить какие элементы не встречаются в другом множестве. При этом необходимо
# сохранить в новую переменную.
z = {1, 2, 3, 4, 5} # множество 1
x = {3, 4, 5, 6, 7} # множество 2
print(z) # OUT: {1, 2, 3, 4, 5}
print(x) # OUT: {3, 4, 5, 6, 7}
t1 = z.difference(x) # другая запись: "set - other_set" 
print(t1) # OUT: {1, 2}

# Метод .difference(). Если пример записать наоборот.
z = {1, 2, 3, 4, 5} # множество 1
x = {3, 4, 5, 6, 7} # множество 2
print(z) # OUT: {1, 2, 3, 4, 5}
print(x) # OUT: {3, 4, 5, 6, 7}
t2 = x.difference(z) # другая запись: "set - other_set" 
print(t2) # OUT: {6, 7}

# ПРИМЕР ИСПОЛЬЗОВАНИЯ МНОЖЕСТВ.

# Сохраним большой блок текста в текстовый файл, используя кодировку "utf-8"
r = open(
	"path_to_file\\New_file3.txt",
	"w", encoding="utf-8") # такого файла нет, поэтому он создается "w", кодировка utf-8
r.write("""Александр Блок — Незнакомка.

По вечерам над ресторанами
Горячий воздух дик и глух,
И правит окриками пьяными
Весенний и тлетворный дух.

Вдали над пылью переулочной,
Над скукой загородных дач,
Чуть золотится крендель булочной,
И раздается детский плач.

И каждый вечер, за шлагбаумами,
Заламывая котелки,
Среди канав гуляют с дамами
Испытанные остряки.

Над озером скрипят уключины
И раздается женский визг,
А в небе, ко всему приученный
Бессмысленно кривится диск.

И каждый вечер друг единственный
В моем стакане отражен
И влагой терпкой и таинственной
Как я, смирен и оглушен.

А рядом у соседних столиков
Лакеи сонные торчат,
И пьяницы с глазами кроликов
«In vino veritas!»* кричат.

И каждый вечер, в час назначенный
(Иль это только снится мне?),
Девичий стан, шелками схваченный,
В туманном движется окне.

И медленно, пройдя меж пьяными,
Всегда без спутников, одна
Дыша духами и туманами,
Она садится у окна.

И веют древними поверьями
Ее упругие шелка,
И шляпа с траурными перьями,
И в кольцах узкая рука.

И странной близостью закованный,
Смотрю за темную вуаль,
И вижу берег очарованный
И очарованную даль.

Глухие тайны мне поручены,
Мне чье-то солнце вручено,
И все души моей излучины
Пронзило терпкое вино.

И перья страуса склоненные
В моем качаются мозгу,
И очи синие бездонные
Цветут на дальнем берегу.

В моей душе лежит сокровище,
И ключ поручен только мне!
Ты право, пьяное чудовище!
Я знаю: истина в вине.
""")
r.close() # закрыть файл

# выведим блок текста на экран, используя кодировку "utf-8"
r = open(
	"path_to_file\\New_file3.txt",
	encoding="utf-8") # открываем файл, кодировка utf-8
#print(r.read()) # закоментировано, т.к. ниже конвертируем и читаем

# сконвертируем из строки текста список при помощи метода .split()
# при этом все пробелы и переносы строки откидываются.
#print(r.read().split()) # закоментировано, т.к. ещё ниже конвертируем и читаем

# сконвертируем список во множество, используя метод .set()
# при этом все повторения слов откинуты.
#print(set(r.read().split())) # двойная конвертация и прочтение файла. Закоментировано, т.к.
# ниже продолжаем работу с файлом.

# Сохраним ЕЩЁ ОДИН большой блок текста в текстовый файл, используя кодировку "utf-8"
r = open(
	"path_to_file\\New_file4.txt",
	"w", encoding="utf-8") # такого файла нет, поэтому он создается "w", кодировка utf-8
r.write("""Александр Блок — В ресторане.

Никогда не забуду (он был, или не был,
Этот вечер): пожаром зари
Сожжено и раздвинуто бледное небо,
И на жёлтой заре — фонари.

Я сидел у окна в переполненном зале.
Где-то пели смычки о любви.
Я послал тебе чёрную розу в бокале
Золотого, как нёбо, аи.

Ты взглянула. Я встретил смущённо и дерзко
Взор надменный и отдал поклон.
Обратясь к кавалеру, намеренно резко
Ты сказала: «И этот влюблён».

И сейчас же в ответ что-то грянули струны,
Исступлённо запели смычки…
Но была ты со мной всем презрением юным,
Чуть заметным дрожаньем руки…

Ты рванулась движеньем испуганной птицы,
Ты прошла, словно сон мой легка…
И вздохнули духи, задремали ресницы,
Зашептались тревожно шелка.

Но из глуби зеркал ты мне взоры бросала
И, бросая, кричала: «Лови!..»
А монисто бренчало, цыганка плясала
И визжала заре о любви.
""")
r.close() # закрыть файл

# вывод блока текста на экран, используя кодировку "utf-8"
r = open(
	"path_to_file\\New_file4.txt",
	encoding="utf-8") # открываем файл, кодировка utf-8
#print(r.read()) # закоментировано, т.к. ниже конвертируем и читаем

# Используем ДВА блока текста.
# Создадим новое множество new, которое будет содержать повторяющиеся слова двух
# блоков текстов (двух стихотворений).
# Множество new содержит все уникальные обьекты, т.е. в этом множестве они
# встечаются один раз.
new = set()

r = open(
	"path_to_file\\New_file3.txt",
	encoding="utf-8") # открываем файл, кодировка utf-8
# обьединить множества. Без сохранения в переменную.
new.update(set(r.read().split())) # другая запись: "set |= other_set"
r.close() # закрыть файл

r = open(
	"path_to_file\\New_file4.txt",
	encoding="utf-8") # открываем файл, кодировка utf-8
 # обьединить множества. Без сохранения в переменную.
new.update(set(r.read().split())) # другая запись: "set |= other_set"
r.close() # закрыть файл

print(new) # вывод всех уникальных слов ДВУХ стихотворений

# Определим какие слова встречаются в обоих стихотворениях.
r = open(
	"path_to_file\\New_file3.txt",
	encoding="utf-8") # открываем файл, кодировка utf-8
i = set(r.read().split()) # обьединить множества. Сохранение в переменную.
r.close() # закрыть файл

r = open(
	"path_to_file\\New_file4.txt",
	encoding="utf-8") # открываем файл, кодировка utf-8
j = set(r.read().split()) # обьединить множества. Сохранение в переменную.
r.close() # закрыть файл

new = i.intersection(j) # другая запись: "set & other_set"
print(new) # вывод всех повторяющихся слов ДВУХ стихотворений

# Найти разницу.
# Эти слова ЕСТЬ во множестве i, при этом их НЕТ во множестве j
r = open(
	"path_to_file\\New_file3.txt",
	encoding="utf-8") # открываем файл, кодировка utf-8
i = set(r.read().split()) # обьединить множества. Сохранение в переменную.
r.close() # закрыть файл

r = open(
	"path_to_file\\New_file4.txt",
	encoding="utf-8") # открываем файл, кодировка utf-8
j = set(r.read().split()) # обьединить множества. Сохранение в переменную.
r.close() # закрыть файл

new = i.difference(j) # другая запись: "set - other_set"
print(new) # вывод всех повторяющихся слов ДВУХ стихотворений


# Найти разницу. Другой вариант.
# Эти слова ЕСТЬ во множестве 'j', при этом их НЕТ во множестве 'i'
r = open(
	"path_to_file\\New_file3.txt",
	encoding="utf-8") # открываем файл, кодировка utf-8
i = set(r.read().split()) # обьединить множества. Сохранение в переменную.
r.close() # закрыть файл

r = open(
	"path_to_file\\New_file4.txt",
	encoding="utf-8") # открываем файл, кодировка utf-8
j = set(r.read().split()) # обьединить множества. Сохранение в переменную.
r.close() # закрыть файл

new = j.difference(i) # другая запись: "set - other_set"
print(new) # вывод всех повторяющихся слов ДВУХ стихотворений
