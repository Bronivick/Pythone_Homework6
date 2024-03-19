# users = ['user1', 'user2', "user3", 'user4', 'user5']
# ids =[4, 5, 9, 14, 7]
# data = list(zip(users,ids))
# print(data)

def print_operation_table(operation, num_rows, num_columns):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*["ОШИБКА! Размерности таблицы должны быть больше 2!" for x in i])


print_operation_table(lambda x, y: x * y, 3, 3)

def print_operation_table(operation, num_rows, num_columns):
    if num_rows<2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return
    res = [[operation(row, col) for row in range(1, num_columns + 1)] for col in range(1, num_rows + 1)]

    for i in res:
        print(*[f"{x} " for x in i])


print_operation_table(lambda x, y: x * y, 3, 3)