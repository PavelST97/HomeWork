# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i это порядковы номер
# строки в списке. Использовать генератор списков.

def sort_list(my_list: list) -> list:
    my_list = [f'{ind} - {my_str}' for ind, my_str in enumerate(my_list)]
    return my_list
