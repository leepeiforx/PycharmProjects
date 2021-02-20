# 关系运算符
print(1 < 2 < 3)
print(1 < 2 > 3)
print(1 < 3 > 2)

# 关系运算符具有惰性计算的特点,只计算必须计算的值,而不是计算关系表达式中的每个表达式

# %%
# 逻辑运算符
3 and 5
3 or 5
0 and 5
0 or 5
not 3
not 0


def Join(chList, sep=None):
    return (sep or '.').join(chList)


def Joinstr(chList, sep=','):
    return sep.join(chList)


chTest = [str(i) for i in range(5)]
Join(chTest, ':')

