import pytest

from conftest import collector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две книги
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('error_book_name', ['', 'Жареные зеленый помидор в кафе Полустанок'])
    def test_add_error_book_add_0_book(self, collector, error_book_name):
        # добавляем книгу
        collector.add_new_book(error_book_name)

        # проверяем, что ничего не добавилось, так как имя книги 0 или более 41 символов
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 0
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_new_book_genre_add_genre(self, collector, genre):
        # добавляем книгу
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # устанавливаем жанр
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', genre)
        # проверяем, что у книги есть жанр
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == genre

    def test_get_books_with_specific_genre_get_book(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # устанавливаем жанры
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        # проверяем, что выводим список книг с определённым жанром
        assert collector.get_books_with_specific_genre('Ужасы') == ['Что делать, если ваш кот хочет вас убить']

    def test_get_books_for_children_get_book(self, collector):
        # добавляем две книги
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Ежик в тумане')
        # устанавливаем жанры
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Ежик в тумане', 'Мультфильмы')
        # проверяем, что возвращаем книгу, подходящую детям
        assert collector.get_books_for_children() == ['Ежик в тумане']

    def test_get_books_not_for_children_dont_get_book_not_for_children(self, collector):
        # добавляем две книги
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Ежик в тумане')
        # устанавливаем жанры
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Ежик в тумане', 'Мультфильмы')
        # проверяем, что не возвращаем книгу, неподходящую детям
        assert collector.get_books_for_children() != ['Что делать, если ваш кот хочет вас убить']

    def test_add_book_in_favorites_book_in_favorites(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем книгу в Избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        # проверяем, что книга в списоке Избранных книг
        assert collector.get_list_of_favorites_books() == ['Что делать, если ваш кот хочет вас убить']

    def test_delete_book_from_favorites_book_is_not_in_favorites(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем книги в Избранное
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        # удаляем книгу из Избранное
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        # проверяем, что книга не в списоке Избранных книг
        assert collector.get_list_of_favorites_books() != ['Что делать, если ваш кот хочет вас убить']

    def test_get_list_of_favorites_books_get_books_list(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем книги в Избранное
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        # проверяем, что книги в списоке Избранных книг
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби',
                                                           'Что делать, если ваш кот хочет вас убить']

    def test_add_new_book_no_genre(self, collector):
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # проверяем, что у добавленной книги нет жанра
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''
