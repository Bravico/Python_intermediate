# 集合与字典表

# set Example and arr Example
# set is {}
# array is []
# dict is a:b

some_list = [1, 2, 3, 4, 5, 1, 4, 8]

even_set = {x for x in some_list if x % 2 == 0}

even_arr = [x for x in some_list if x % 2 == 0]

print(even_set)
print(even_arr)

# Dict Example, Range()函数

d = {x: x % 2 == 0 for x in range(1, 11)}

print(d)
