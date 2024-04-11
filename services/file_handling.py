import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    separators = [',', '.', '!', ':', ';', '?']
    if len(text) < start + size:
        size = len(text) - start
        a = text[start:start + size]
    else:
        a = text[start:(start + size)]
        while (a[-1] not in separators) or (a[-1] in separators and text[start:(start + size + 1)][-1] in separators):
            size -= 1
            a = text[start:(start + size)]
    return a, len(a)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(file=path, mode='rt', encoding='utf-8') as my_file:
        text = my_file.read()
    start = 0
    i = 1
    while start < len(text):
        page_text, size = _get_part_text(text, start, PAGE_SIZE)
        book[i] = page_text.lstrip()
        i += 1
        start += size


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))