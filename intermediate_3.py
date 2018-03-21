# Counter的使用方式和import的用法
# may occur the problem of ValueError in terms of the String type of Dict
# ValueError: dictionary update sequence element #0 has length 1; 2 is required

# from collections import Counter
# ------------------------------
# import collections as cc

# import collections

# from collections import Counter
# c = Counter("abcdefgab")
#
# print(c)

import collections as cc

c = cc.Counter("abcdefgab")
# print(c["b"])
print(c)
print(c.most_common(2))