from book import BookFactory
from biblioteka import Library, Librarian

class People:
    def __init__(self):
        self.last_name = None
        self.first_name = None
        self.user_card = dict()
        self.membership_number = 0

    def create_user(self):
        while True:
            self.last_name = input(f'\nДля заполнения базы данных читателей '
                                   f'введите фамилию или 0, что бы закончить ввод\n'
                                   f'-> ').title()
            if self.last_name == "0":
                break
            self.first_name = input(f'Введите имя читателя\n'
                                    f'-> ').title()
            self.membership_number += 1
            self.user_card[self.membership_number] = [self.last_name, self.first_name]
        return self.user_card

    def verification(self):
        self.name_verefication = None
        name = input(f'Введите вашу фамилию и имя\n'
                     f'-> ').title()
        if name in self.user_card[self.membership_number]:
            print(f'Пользователь с такими данными есть в базе. Вы можете заказать книгу.')
            self.name_verefication = True
        else:
            print(f'Извините, но пользователя с такими данными нет в базе нашей библиотеки, '
                  f'вам нужно пройти в администрацию.')
            self.name_verefication = False

library = Library()
print(library, '\n')
librarian1 = Librarian('Марь Иванна')
librarian2 = Librarian('Евгения Барисовна')
librarian3 = Librarian('Евдакинья Георгевна')
print('Сотрудники:')
for i in (librarian1, librarian2, librarian3):
    print(i)

people = People()
print(people.create_user())
people.verification()
if people.name_verefication == True:
    people = BookFactory()
    people.create_book()


