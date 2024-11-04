class Publisher:
    def __init__(self, title, publisher, year, pages):
        self.title = title
        self.publisher = publisher
        self.year = year
        self.pages = pages

    def get_info(self):
        return f"Название: {self.title}, Издатель: {self.publisher}, Год: {self.year}, Страниц: {self.pages}"
    
class Paper(Publisher):
    def __init__(self, title, publisher, year, pages, edition, section):
        super().__init__(title, publisher, year, pages)
        self.edition = edition
        self.section = section

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип издания: {self.edition}, Разделы: {', '.join(self.section)}"

class Book(Publisher):
    def __init__(self, title, publisher, year, pages, author, genre):
        super().__init__(title, publisher, year, pages)
        self.author = author
        self.genre = genre

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Автор: {self.author}, Жанр: {self.genre}"


class Periodic(Publisher):
    def __init__(self, title, publisher, year, pages, frequency):
        super().__init__(title, publisher, year, pages)
        self.frequency = frequency

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Частота выпуска: {self.frequency}"



paper = Paper("Ежедневные новости", "Издательство Пресс", 2023, 24, "ежедневная", ["Политика", "Экономика", "Спорт"])
book = Book("Программирование на Python", "Издательство Код", 2021, 350, "Джон До", "Образование")
magazine = Periodic("Наука и жизнь", "Научное издательство", 2023, 50, "ежемесячно")
print(paper.get_info())
print(book.get_info())
print(magazine.get_info())