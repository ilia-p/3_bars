# Ближайшие бары

Скрипт загружает информацию о барах в формате json и возвращает бар c максимальным/минимальным количеством мест и ближайшие бары по введенным текущим координатам.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 и библиотеки geopy версии 1.11.0 для вычисления расстояний по координкатам.

Запуск на Windows: `>python bars.py -p data-2897-2016-11-23.json`

Результат работы скрипта

```
Бар(ы) с наименьшим количесвом мест:
Бар «Витамин»
Клуб ДИЧ
Попкорн Бар
Бар «Стабильная линия»
Пивбар
ПивБар
Бар 365
Лоби-бар «Галерея»

Бар(ы) с наибольшим количесвом мест:
Спорт бар «Красная машина»

Введите долготу: 37.58720622581923
Введите широту: 55.777682317891

Ближайший(е) бар(ы):
ЛОББИ-БАР
БЕЛОЧКА
HAGGIS

```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
