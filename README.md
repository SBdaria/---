h1 Описание проекта
=====================
h2 Основной функционал:
-----------------------------------
1. Программа загружает данные из всех прайс-листов (файлы, в названии которых есть слово "price"), обрабатывая только стобцы с наимеованием, весом и ценой товара. Остальные столбцы игнорируются.
Предполагается, что столбец с названием товара называется одним из вариантов: "название", "продукт", "товар", "наименование".
Столбец с ценой может называться "цена" или "розница".
Столбец с весом имеет название "фасовка", "масса" или "вес" и всегда указывается в килограммах.
<img width="207" alt="image" src="https://github.com/user-attachments/assets/1c03f0f4-fd25-4d6b-b1e8-efcd1887b291" />

<img width="677" alt="image" src="https://github.com/user-attachments/assets/d93a7f8a-defa-4efb-8c72-5c982e0f2a02" />


2. Есть возможность циклического поиска товара по фрагменту названия с сорторовкой по цене за килогорамм. Поиск будет происходить до тех пор, пока пользователь не введет "exit".
Отобранные данные выводятся в консоль в виде таблицы.
<img width="596" alt="image" src="https://github.com/user-attachments/assets/faac05e7-a57d-4a71-97d4-234d249362e0" />

3. При завершении работы программа выгружает данные всех прайс-листов в файл html.
<img width="1007" alt="image" src="https://github.com/user-attachments/assets/103f215f-b4a1-4503-b333-fc5a8916263f" />

<img width="841" alt="image" src="https://github.com/user-attachments/assets/70716ed0-7fe2-4ffa-88be-85da3b417978" />

h2 Как запустить
-----------------------------------
1. Склонируйтке проект и перейдите в директорию проекта.
2. Установите необходимые библиотеки выполнив следующую команду: pip install -r requirements.txt.
3. Запустите код с помощью данной команды: python main.py




