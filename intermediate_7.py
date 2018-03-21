# filter usage
# slicer && range

def is_odd(n):
    return n % 2 == 1


# filter的用法, 类似于map&&reducer
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# --------------------------------Q1--------------------------------------------

# 回数是指从左向右和从右向左读都是一样的数，例如 12321，909。请利用 filter() 滤掉非回数：

def is_palindrome(n):
    return str(n) == str(n)[::-1]


print(list(filter(is_palindrome, list(range(1000)))))

# --------------------------------ext--------------------------------------------
# --------------------------------切片--------------------------------------------

print('ABCDEFG'[::-1])  # 倒序
print('ABCDEFG'[::2])  # 相差为1

# --------------------------------快速生成list，range的用法--------------------------------------------
L = list(range(100))
print(L)
