import re
import urllib.request
import html


class WebPage:

    def __init__(self, url):
        self.url = url
        self.html = ''
        self.title = ''
        self.text = ''

    # парсим саму страничку
    def fetch(self):
        try:
            response = urllib.request.urlopen(self.url)
            self.html = response.read().decode('utf-8')
        except Exception as e:
            print('Ошибка ссылки: ', e)
            exit()

    def parse(self):
        # Находим заголовок статьи
        match = re.search(r'<title[^>]*>(.*?)</title>', self.html, re.DOTALL)
        if match:
            self.title = html.unescape(match.group(1).strip())

        # Чистим html код от посторонних тегов
        del_rubbish = re.sub(r'<head>.*?</head>', '', self.html, flags=re.DOTALL)
        # region да, понимаю что избытоная проверка, но на сайте газета ру иначе фоторгафии не удаляются
        del_rubbish = re.sub(r'<!--.*?->', '', del_rubbish, flags=re.DOTALL)
        del_rubbish = re.sub(r'<img(.*?)>', '', del_rubbish, flags=re.DOTALL)
        del_rubbish = re.sub(r'<span(.*?)>', '', del_rubbish, flags=re.DOTALL)
        # endregion
        del_rubbish = re.sub(r'<script(.*?)>(.*?)</script>', '', del_rubbish, flags=re.DOTALL)
        del_rubbish = re.sub(r'<noscript(.*?)>(.*?)</noscript>', '', del_rubbish, flags=re.DOTALL)
        del_rubbish = re.sub(r'<style(.*?)>(.*?)</style>', '', del_rubbish, flags=re.DOTALL)
        del_rubbish = re.sub(r'<nostyle(.*?)>(.*?)</nostyle>', '', del_rubbish, flags=re.DOTALL)
        del_rubbish = re.sub(r'<iframe(.*?)>(.*?)</iframe>', '', del_rubbish, flags=re.DOTALL)
        # Заменяем спец. символов HTML
        del_rubbish = html.unescape(del_rubbish)

        # Форматируем текст
        self.text = re.sub(r'<.*?>', '', del_rubbish)  # удаляем теги HTML
        # TODO: я не понимаю почему на этом моменте он не всегда удаляет теги
        self.text = re.sub(r'\n+', '\n', self.text)  # заменяем множественные пробелы на один
        self.text = re.sub(r'(\S{20})\s', r'\1\n', self.text)  # переносим строки по словам

    # запись в файл
    def save_to_file(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(self.title + '\n\n')
            file.write(self.text)


# region Ссылки
# https://habr.com/ru/articles/349860/#Regulyarki
# https://lenta.ru/news/2023/04/06/peskov_bel/
# https://www.gazeta.ru/politics/news/2023/04/09/20172823.shtml?updated
# https://docs.telethon.dev/en/stable/basic/quick-start.html
# https://shootnick.ru/ip_calc/9.172.16.1/16
# endregion

if __name__ == '__main__':
    url = 'https://www.gazeta.ru/politics/news/2023/04/09/20172823.shtml?updated'
    web_page = WebPage(url)
    web_page.fetch()
    web_page.parse()
    web_page.save_to_file(re.sub(r"\W+", "_", web_page.title) + '.txt')
