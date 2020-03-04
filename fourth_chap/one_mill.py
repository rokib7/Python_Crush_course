import sys

empty_list = []
list_size = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))
print(numbers)
print(list_size)
print(type(numbers))
print(type(list_size))

size = sys.getsizeof(numbers)
new_size = sys.getsizeof(list_size)
empty_list_size = sys.getsizeof(empty_list)
print(size)
print(new_size)
print(empty_list_size)
