#  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, 
# т.е. функцию двух аргументов. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны.
#  Нумерация строк и столбцов идет с единицы.

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        res = []
        for j in range(1, num_columns + 1):
            res.append(str(operation(i, j)))
        print(''.join(f'{i:<3}' for i in res))
 
print_operation_table(lambda x, y: x * y)
