# sorted usages

# --------------------------------Q1--------------------------------------------
# 用sorted()对列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# print(sorted(L.keys(),key=str.lower))


def by_name(t):
    return t[0].lower()


L1 = sorted(L, key=by_name)
print(L1)