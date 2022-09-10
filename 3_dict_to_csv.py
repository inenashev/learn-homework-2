"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    data = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Петр', 'age': 38, 'job': 'Small boss'}
    ]
    import csv

    with open('data.csv','w',encoding='utf-8',newline='') as csv_file:
        fields = data[0].keys()
        writer = csv.DictWriter(csv_file, fields, delimiter=',')
        for element in data:
            writer.writerow(element)

if __name__ == "__main__":
    main()
