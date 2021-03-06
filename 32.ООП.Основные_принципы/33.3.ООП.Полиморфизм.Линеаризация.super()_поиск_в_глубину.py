# Python_Hub_Studio
# Python ООП уроки для начинающих с нуля, курс python ООП за три урока.
# Урок_№2.Полиморфизм.

# Полиморфизм. Метод a() вылняет разные функции, когда используется в другом классе.
class A():
	def a(self):
		print("A")


class B():
	def a(self):
		print("B")


class C(B):
	def a(self):
		print("C")


class D(C, A):
	def a(self):
		super().a()
		print(self.__class__.__mro__)


# Закомментируем print() в классе D и запустим метод a() класса D
# Отрабатывает метод a() класса C, потому что метод супер нашел первым его
# Поиск при помощи метода super() в классах родителях называется ЛИНЕАРИЗАЦИЯ
D().a() # OUT: C

# Если раскомментировать print() в классе D , то можно посмотреть как именно Python осуществляет поиск из
# наследуемых классов.

# Так реализован наглядно ПОИСК В ГЛУБИНУ
# OUT: (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(D.__mro__)
# сначала обращаемся к <class '__main__.C'>, затем к <class '__main__.B'>, а затем только <class '__main__.A'>


# Способ, который позволяет выставить жесткую привязку методу super().
class E(C, A):
	def a(self):
		super(C, self).a()

# Внутри метода super() прописан класс 'C', значит метод будет искать ОТ класса 'C', а именно сразу полезет в 'B'
E().a() # OUT: B
