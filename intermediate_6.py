# map/ reducer
from functools import reduce


# ---------------------------------Q1-------------------------------------
# 利用map()函数，把用户输入的不规范的英文名字，
# 变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

# format the first letter to upper letter

# --------------------------------Answer1--------------------------------
def format_first_letter(s):
    return s.capitalize()


keys = map(format_first_letter, ['adam', 'LISA', 'barT'])

for key in keys:
    print(key)

# ----------------------------------Ext------------------------------------
# Filename : test.py
# str的字母切换
# author by : www.runoob.com

str = "www.runoob.com"
print(str.upper())  # 把所有字符中的小写字母转换成大写字母
print(str.lower())  # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())  # 把第一个字母转化为大写字母，其余小写
print(str.title())  # 把每个单词的第一个字母转化为大写，其余小写


# ----------------------------------Q2------------------------------------
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def fn(x, y):
    return x * y;


print(reduce(fn, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 接受用户的输入

input("请输入数字：\n")
val = input()
print(val)

# -----------------------------------Q3-----------------------------------
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(s):
    ss = s.split(".")
    l1, l2 = list(map(int, ss[0])), list(map(int, ss[1]))
    f1, f2 = reduce(fn1, l1), reduce(fn1, l2) / 10 ** len(l2)
    return f1+f2


def fn1(x, y):
    return x * 10 + y


def fn2(x, y):
    return x


def char2num(s):
    return DIGITS[s]

print(str2float('123.456'))