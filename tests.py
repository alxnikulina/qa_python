from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_rating_cant_set_rating_for_missing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Generation П")
        assert collector.get_book_rating("Generation П") == 1

    def test_set_rating_cant_set_rating_for_unexisting_book(self):
        collector = BooksCollector()
        collector.set_book_rating("Чапаев и Пустота", 5)
        assert collector.get_book_rating("Чапаев и Пустота") is None

    def test_add_new_book_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Чапаев и Пустота")
        assert collector.get_book_rating("Чапаев и Пустота") == 1

    def test_add_favorite_book_unadded_book_has_no_rating(self):
        collector = BooksCollector()
        book_name = "Generation П"
        collector.add_book_in_favorites(book_name)
        assert book_name not in collector.favorites

    def test_add_boo_in_favorites_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = "Generation П"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name in favorites

    def test_add_book_in_favorites_cannot_add_book_in_favorites_if_not_in_books_rating(self):
        collector = BooksCollector()
        book_name = "Ampire V"
        assert collector.add_book_in_favorites(book_name) == False

    def test_remove_from_favorites_remove_book_from_favorites(self):
        collector = BooksCollector()
        book_name = "Ampire V"
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, 5)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.books_rating
