# 二项分布概率的计算
from scipy import stats

n = 6
p = 0.3

# 1.恰有4个顾客购买
k = 4
prob = stats.binom.pmf(k, n, p)

# 2.购买的顾客不超过一半
k = 3
prob = stats.binom.cdf(k, n, p)
prob = 1 - (stats.binom.pmf(4, n, p) + stats.binom.pmf(5, n, p) + stats.binom.pmf(6, n, p))

# 3. 至少有1个顾客购买，相当于1 - 没有买的的概率
prob = 1 - stats.binom.cdf(0, n, p)
# %%
# 泊松分布概率计算
# 某航空公司的订票处每60分钟有48次电话。求5分钟内接到3次电话的概率。
x = 3
mu = (48 / 60) * 5
prob = stats.poisson.pmf(x, mu)

# %%
# 超几何分布概率计算
"""利用scipy统计模块计算超几何分布概率 10人中，6人喜欢可口可乐，4人喜欢百事可乐，
从这些人中选出一个3人的随机样本。求
1.恰有2人喜欢可口可乐的概率是多少？
2.2或3个人喜欢百事可乐的概率是多少？
简单理解超几何分布:它描述了从有限M个物件（其中包含n个指定种类的物件）中抽出N个物件，
成功抽出该指定种类的物件的次数（不放回）。"""

N = 3
M = 10
m = 6  # 这里是6人喜欢可口可乐的意思

# 1.恰有2人喜欢可口可乐的概率是多少？
k1 = 2
prob = stats.hypergeom.pmf(k1, M, m, N)

# 2或3个人喜欢百事可乐的概率是多少？
k2 = 3
n = 4  # 这里是4人喜欢百事
prob = stats.hypergeom.pmf(k1, M, 4, N) + stats.hypergeom.pmf(k2, M, 4, N)

# %%
# 正态分布概率计算
"""
人们第一次结婚的平均年龄是26岁。假设第一次结婚的年龄为正态分布，标准差为4年。求
"""
# 1.一个人第一次结婚时的年龄小于23岁的概率多大？
mu = 26
sigma = 4
x1 = 23
prob = stats.norm.cdf(x1, mu, sigma)

# 2.一个人人第一次结婚时的年龄在20-30岁之间的概率多大？
x1, x2 = 20, 30
prob = stats.norm.cdf(x2, mu, sigma) - stats.norm.cdf(x1, mu, sigma)

# 3.95%的人在什么年龄前第一次结婚
p = 0.95
age = stats.norm.ppf(p, mu, sigma)

# %%
# 实验3-5 卡方分布概率计算
"""
利用scipy.stats.chi2进行计算 from scipy import stats stats.chi2.cdf(x,n) stats.chi2.pdf(x,n)
cdf返回随机变量X小于x的累积概率，即P(X"""

# %%
# 排列组合与阶乘函数计算概率
