# Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий. Реализовать
# CRUD(создание, чтение, обновление по id, удаление по id) для продуктов. Создать пользовательский
# интерфейс(использовать разделение логики по модулям - ui отдельно, работа с БД отдельно, запуск
# программы из консоли отдельно и т.д. в зависимости от логики приложения).
import sqlite3

conn = sqlite3.connect('products.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS products(
    post_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    comment TEXT NOT NULL );
""")


def append_product():
    count = 0
    my_data = []
    text = ['post_id', 'name', 'price', 'quantity', 'comment']
    print('Введите данные: ')
    while count < 5:
        my_data.append(input(text[count] + '->'))
        count += 1
    cur.execute("INSERT INTO products VALUES(?, ?, ?, ?, ?);", tuple(my_data))
    conn.commit()


def deleted_product():
    product_id = input('Введите ид продукта, который вы хотите удалить: ')
    cur.execute(f"DELETE FROM products WHERE post_id = {product_id}")
    conn.commit()


def update():
    product_id = input('Введите ид продукта: ')
    column = input('Введите название столбца, который вы хотите изменить: ')
    text = str(input('Введите данные для изменения: '))
    cur.execute(f"UPDATE products SET {column} = {text} WHERE post_id = {product_id}")
    conn.commit()


def main():
    print('''Добавление продукта -> 1
Удаление продукта -> 2
Обновление данных -> 3
Выход из программы -> 0''')
    # cur.execute(".mode column")
    # cur.execute("SELECT * FROM products")
    number_program = int(input('Введите номер программы: '))
    while number_program != 0:
        if number_program == 1:
            append_product()
        elif number_program == 2:
            deleted_product()
        elif number_program == 3:
            update()
        elif number_program == 4:
            pass
        number_program = int(input('Введите номер программы: '))


if __name__ == '__main__':
    main()
