immutable_var = 1, 2, "Sun", True, 5.55
print(immutable_var)
# immutable_var[2][2] = 'Universe'
print(immutable_var) # нельзя изменять данные кортежа, так как данные в нем являются неизменяемыми

immutable_list = [5, 7, "Sun", False, 11.11] # создаем список, списки это изменяемый тип данных
print(immutable_list)
immutable_list[2] = "Moon"
print(immutable_list) # был создан как изменяемый список, потому можно менять содержимое
immutable_list[4] = 5.55
print(immutable_list)
immutable_list[3] = True
print(immutable_list)

