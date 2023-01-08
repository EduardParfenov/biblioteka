########## Урок 39 ##########

########## Паттерн Стратегия

# Создайте приложение для приготовления пасты. Приложение должно уметь создавать
# минимум три вида пасты.
# Классы различной пасты должны иметь следующие методы:
# - Тип пасты
# - Соус
# - Начинка
# - Добавки

# from abc import ABC, abstractmethod
#
# class Strategy(ABC):
#     @abstractmethod
#     def type(self):
#         pass
#
#     @abstractmethod
#     def nachinka(self):
#         pass
#
#     @abstractmethod
#     def dobavka(self):
#         pass
#
#     @abstractmethod
#     def sous(self):
#         pass
#
# class Farfalle(Strategy):
#     def type(self):
#         return "Фарфале спагетти"
#
#     def nachinka(self):
#         return "Спагети, бекон, сыр"
#
#     def dobavka(self):
#         return "Двойная порция сыра"
#
#     def sous(self):
#         return "Двойная порция сыра"
#
# class Karbanara(Strategy):
#     def type(self):
#         return "Длинные спагетти"
#
#     def nachinka(self):
#         return "Спаггети, бекон, сыр"
#
#     def dobavka(self):
#         return "Двойная порция сыра"
#
#     def sous(self):
#         return "Соус со сливками"
#
# class Context:
#     def setStrategy(self, strategy=None):
#         if strategy is not None:
#             self.strategy = strategy
#         else:
#             self.strategy = Karbanara()
#
#     def executeStrategy(self):
#         print("Состав пасты: ")
#         print(self.strategy.type())
#         print(self.strategy.nachinka())
#         print(self.strategy.dobavka())
#         print(self.strategy.sous())
#         print()
#
# pasta1 = Context()
# pasta2 = Context()
#
# pasta1.setStrategy(Karbanara())
# pasta2.setStrategy(Farfalle())
#
# pasta1.executeStrategy()
# pasta2.executeStrategy()

########## Фабричный метод

# from abc import ABC, abstractmethod
#
# class Paste:
#     def __init__(self, paste_all=None):
#         self.paste_all = paste_all
#
#     def show_paste(self):
#         paste = self.paste_all()
#
#         print("Состав пасты: ")
#         print(paste.type())
#         print(paste.nachinka())
#         print(paste.dobavka())
#         print(paste.sous())
#         print()
#
# class Strategy(ABC):
#     @abstractmethod
#     def type(self):
#         pass
#
#     @abstractmethod
#     def nachinka(self):
#         pass
#
#     @abstractmethod
#     def dobavka(self):
#         pass
#
#     @abstractmethod
#     def sous(self):
#         pass
#
# class Farfalle(Strategy):
#     def type(self):
#         return "Фарфале спагетти"
#
#     def nachinka(self):
#         return "Спаггети, бекон, сыр"
#
#     def dobavka(self):
#         return "Двойная порция сыра"
#
#     def sous(self):
#         return "Двойная порция сыра"
#
# class Karbanara(Strategy):
#     def type(self):
#         return "Длинные спагетти"
#
#     def nachinka(self):
#         return "Спаггети, бекон, сыр"
#
#     def dobavka(self):
#         return "Двойная порция сыра"
#
#     def sous(self):
#         return "Соус со сливками"
#
# array = [Farfalle, Karbanara]
#
# for i in array:
#     paste = Paste(i)
#     paste.show_paste()

##########

# Создайте приложение для работы в библиотеке. Оно должно оперировать
# следующими сущностями: Книга, Библиотекарь, Читатель. Приложение должно
# позволять вводить, удалять, изменять, сохранять в массив, загружать из массива,
# логгировать действия, искать информацию (результаты поиска выводятся на
# экран или файл) о сущностях. При реализации используйте максимально возможное
# количество паттернов проектирования.

# from abc import ABC, abstractmethod
#
# class Books(ABC):
#     def __init__(self):
#         self.books_dict = dict()
#
#     @abstractmethod
#     def type_book(self):
#         pass
#
#     def add_book(self):
#         new_book = input('Введите название книги ')
#         book_amount = input('Сколько копий? \n').strip()
#
#         assert book_amount.isdigit(), 'Нужно ввести число'
#         book_amount = int(book_amount)
#
#         if new_book not in self.books_dict:
#             self.books_dict[new_book] = book_amount
#         else:
#             self.books_dict[new_book] += book_amount
#
#     def __getitem__(self, item):
#         return self.books_dict[item]
#
#     def __str__(self):
#         return ''.join(f'Название книги: {key}, количество: {value}\n' for key, value in self.books_dict.items())
#
# class Fantasy(Books):
#     def type_book(self):
#         return 'Фэнтези'
#
# class Roman(Books):
#     def type_book(self):
#         return 'Романы'
#
# class Horror(Books):
#     def type_book(self):
#         return 'Ужасы'
#
# class BookFactory:
#     def __init__(self):
#         self.all_books = {'Романы': list(),
#                           'Фэнтези': list(),
#                           'Ужасы': list()}
#
#     def create_book(self):
#         current_books = {'Романы': Roman,
#                          'Фэнтези': Fantasy,
#                          'Ужасы': Horror}
#         book_genre = input('Укажите жанр который вас интересует: \n').strip().title()
#         if book_genre in current_books:
#             new_book = current_books[book_genre]()
#             new_book.add_book()
#             books = self.all_books[book_genre]
#             books.append(new_book)
#             return new_book
#         else:
#             print('У нас нет такого жанра.')
#
#     def check_books(self):
#         for book_genre, books in self.all_books.items():
#             print(f'{book_genre}\n'
#                   f'{" ".join(map(str, books))}')
#
# new_factory = BookFactory()
# book1 = new_factory.create_book()
# book2 = new_factory.create_book()
# book3 = new_factory.create_book()
# new_factory.check_books()


