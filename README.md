# parser
Используемые встроенные модули питона: re, urllib.request, html

Алгоритм:
1) Непосредственный парсинг и получение html кода страницы методом fetch
2) Чистка и преобразование html кода методом parse
3) Сохранение результата в файл методом save_to_file

Недостатки:
1) Почему-то не на всех сайтах срабатывает "чистка" от ненужных тегов
2) Получаемый файл не сильно приятен глазу для чтения

Также в проекте в файле tricky_solution описан код, который преобразует html код в формат Markdown, хоть и с использованием сторонней бибилотеки
