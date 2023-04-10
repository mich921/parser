import urllib.request
import html2text


# TODO решение задачи, но с использованием сторонней библиотеки
class HTMLtoMD:
    def __init__(self, url, file_path):
        self.url = url
        self.file_path = file_path

    def parse_and_save(self):
        # Получаем HTML страницу
        response = urllib.request.urlopen(self.url)
        html_page = response.read().decode('utf-8')

        # Инициализируем html2text и преобразуем HTML в Markdown
        h = html2text.HTML2Text()
        markdown_text = h.handle(html_page)

        # Записываем результат в файл
        with open(self.file_path, "w", encoding='utf-8') as f:
            f.write(markdown_text)


converter = HTMLtoMD(url="https://lenta.ru/news/2023/04/06/peskov_bel/", file_path="example.md")
converter.parse_and_save()
