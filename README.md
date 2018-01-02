# Ближайшие бары

Скрипт выводит название самого большого, маленького и ближайшего к вашему местоположению бара Москвы

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

* Скачайте файл [bars.json](https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json) и поместите его в корневую папку скрипта
* Запустите файл bars.py, укажите аргумент -file и название файла с расширением
* Укажите ваши gps-координаты: широту и долготу


Запуск на Linux:
```
$ python bars.py -file bars.json
Введите значение долготы: 37
Введите значение ширины: 55
Самый большой бар: Спорт бар «Красная машина»
Cамый маленький бар: БАР. СОКИ
Ближайший бар: Бар «Адамов Роман Анатольевич»
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
