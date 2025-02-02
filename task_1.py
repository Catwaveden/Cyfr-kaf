class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, new_name: str) -> None:
        if isinstance(new_name, str):
            self.name = new_name
        else:
            raise ValueError("Название должно быть типа str")

    @property
    def author(self) -> str:
        return self.author

    @author.setter
    def author(self, new_author: str) -> None:
        if isinstance(new_author, str):
            self.author = new_author
        else:
            raise ValueError("Имя автора должно быть типа str")



class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> str:
        return self.pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not(isinstance(new_pages, int)):
            raise TypeError("Количество страниц должно быть типа int")
        elif new_pages < 0:
            raise ValueError("Количество страниц должно быть положительным")
        else:
            self.pages = new_pages



class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self) -> float:
        return self.duration

    @duration.setter
    def pages(self, new_duration: float) -> None:
        if not(isinstance(new_duration, float)):
            raise TypeError("Длительность аудиокниги должна быть типа float")
        elif new_duration < 0:
            raise ValueError("Длительность аудиокниги должна быть положительной")
        else:
            self.duration = new_duration