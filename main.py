tuple_ = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tuple_1 = ([0, 1], [2, 3], [4, 5], [6, 7], [8, 9])
print('Количество занятой памяти в tuple: ', tuple_.__sizeof__())
print('Количество занятой памяти в list: ', list_.__sizeof__())
print('Количество занятой памяти в (tuple[list]): ', tuple_1.__sizeof__())
print('Количество элементов во всех хранилищай одинаковое')
print('Пример работы с (tuple[list]): ', tuple_1 [2] [1])

# Чтобы освободить память компьютера, что приводит к более быстрому выполнению программ, list заменяется на tuple.
# Это уже освобождает память, но чтобы можно было так же свободно работать как с list, все элементы в tuple берутся в list, по 2 элемента.
# Таким образом мы получаем тот же функционал что и у list, но с той же особенностью занимания меньшего объема памяти что и у tuple, так еще и в 2 раза меньше.
# Единственная, на мой взгляд проблема, более сложная работа с элементами.

