import os
import csv
import pandas as pd


class PriceMachine():

    def __init__(self):
        self.df = None
        self.data = []

    def load_prices(self, file_path='pricelists'):
        '''
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт

            Допустимые названия для столбца с ценой:
                розница
                цена

            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        '''
        files = os.listdir(file_path)
        for file in files:
            if 'price' in file:
                with open(f'{file_path}/{file}') as f:
                    reader = csv.reader(f)
                    headers = [i.lower() for i in next(reader)]

                    columns = self._search_product_price_weight(headers)
                    for row in reader:
                        self.data.append([row[columns[0]].lower(), int(row[columns[1]]), int(row[columns[2]]), file,
                                          round(float(row[columns[1]]) / float(row[columns[2]]), 2)])
        self.df = pd.DataFrame(self.data, columns=['Наименование', 'цена', 'вес', 'файл', 'цена за кг.'], copy=True)
        pd.options.display.max_rows = None
        pd.options.display.expand_frame_repr = False
        self.df.index += 1
        return self.df

    def _search_product_price_weight(self, headers):
        '''
            Возвращает номера столбцов
        '''
        columns = []
        names_columns = ['товар', 'название', 'наименование', 'продукт', 'розница', 'цена', 'вес', 'масса',
                         'фасовка']
        for col in names_columns:
            if col in headers:
                columns.append(headers.index(col))
        return columns

    def export_to_html(self, fname='output.html'):
        result = '''
        <!DOCTYPE html>
        <html>
        <body>
            <table BORDER=1 width="60%">
                <CAPTION ALIGN=top><h2>Позиции продуктов</h2></CAPTION>
                    <tr>
                        <th ALIGN=center width="10%">Номер</th>
                        <th ALIGN=center width="40%">Название</th>
                        <th ALIGN=center width="15%">Цена</th>
                        <th ALIGN=center width="10%">Вес(кг)</th>
                        <th ALIGN=center width="10%">Файл</th>
                        <th ALIGN=center width="15%">Цена за кг.</th>
                    </tr>
        '''
        for number, item in enumerate(self.data):
            product_name, price, weight, file_name, value = item
            result += '<tr>\n'
            result += f'<td ALIGN=center>{number + 1}</td>\t'
            result += f'<td ALIGN=left>{product_name}</td>\t'
            result += f'<td ALIGN=center>{price}</td>\t'
            result += f'<td ALIGN=center>{weight}</td>\t'
            result += f'<td ALIGN=center>{file_name}</td>\t'
            result += f'<td ALIGN=center>{value}</td>\n'
            result += '</tr>\n'
        with open(fname, 'w', encoding='utf-8') as file:
            file.write(result)
        return 'Данные всех плайс-листов занесены в файл "output.html".'

    def find_text(self, text):
        search = self.df[self.df['Наименование'].str.contains(text)]
        if search.empty:
            return 'Такого товара в плайслистах нет.'
        search = search.sort_values(by='цена за кг.')
        pd.options.display.max_rows = None
        pd.options.display.expand_frame_repr = False
        search = search.reset_index()
        del search['index']
        search.index += 1
        return search


pm = PriceMachine()
pm.load_prices()

while True:
    name_product = input('Введите название продукта или "exit" для завершения процесса поиска: ').lower()
    if name_product == 'exit':
        break
    else:
        print(pm.find_text(name_product))

print('Поиск завершен!')
print(pm.export_to_html())
