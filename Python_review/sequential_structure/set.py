# 集合的创建与删除
a = {3, 5}  # 创建集合对象
type(a)

'''也可以使用set()函数将列表,元组,字符串,range对象等其他可迭代对象转换为集合,如果原来的数据中存在重复元素,
则在转换为集合时只保留一个;如果原序列或迭代对象中有不可哈希的值,无法转换为集合,抛出异常'''
a_set = set(range(8, 14))  # 把range对象转换为集合
b_set = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 1, 2, 3])
print(b_set)

# %%
# 集合推导式
c_set = {x.strip() for x in ('he ', 'she ', ',', 'I')}
print(c_set)

# %%
# 集合操作与删除
# add() 增加新元素,若元素存在则忽略该操作
# update()方法合并另一个集合的元素到当前集合中,并去重

a_set = {1, 2, 3}
a_set.add(3)
a_set.update([1, 3, 4, 6, 7, 8])
a_set

# pop() 随机删除并返回集合中的一个元素,集合为空则抛出异常
print(a_set.pop())
a_set
# remove()删除集合中的元素,如果元素不存在则抛出异常
a_set.remove(2)
a_set
# discard()从集合中删除一个特定的元素,如果元素不存在则忽略该操作
a_set.discard(2)
a_set
# clear()清空集合

# %%
# 集合运算
'''内置函数len,max,min,sum,sorted,map,filter,enumerate等也适用于集合.
另外,python集合还支持数学意义上的交集,并集,补集,差集等运算'''

a_set = set(range(8, 14))
b_set = set(range(0, 12, 2))
# 并集
a_set | b_set
a_set.union(b_set)
# 交集
a_set & b_set
a_set.intersection(b_set)
# 差集
a_set.difference(b_set)
a_set - b_set
# 对称差集
a_set.symmetric_difference(b_set)
# 比较集合的大小/包含关系
x = {1, 2, 3}
y = {1, 2, 5}
z = {1, 2, 3, 4}

x < z  # 真子集
{1, 2, 3} <= {1, 2, 3}  # 子集

x.issubset(y)  # 测试是否是子集
x.issubset(z)

{3} & {4}
{3}.isdisjoint({4})  # 如果两个集合的交集为空,返回True
'''关系元算符>,>=,<,<=作用于集合时表示集合之间的包含关系,而不是比较集合中元素的大小关系.'''

# %%
# 不可变集合frozenset
# frozenset中不提供add,remove等修改集合内容的方法
x = frozenset(range(5))
# x.add(5)
# 并集运算
x | frozenset(range(5, 10))
# 交集运算
x & frozenset(range(5, 10))
# 差集运算
x - frozenset(range(5, 10))
# 集合包含关系比较
frozenset(range(4)) < frozenset(range(5))
