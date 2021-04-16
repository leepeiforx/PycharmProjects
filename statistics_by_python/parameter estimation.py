# 参数估计
'''
享受贷款的学生毕业前欠款平均数额为12168美元，假定这一欠款数额的平均值是基于
480名学生贷款人组成的样本计算得来的，
毕业前欠款数额的总体标准差为2200美元。根据样本数据给出学生中享受贷款的在
毕业前平均欠款数额的95%的置信区间。
注意，大于30即为大样本。
'''
import numpy as np
import pandas as pd
from scipy import stats

# %%
# 这些是已知数据
confidence = 0.95
sample_mean = 12168
sample_n = 480
pop_std = 2200

# 抽样平均误差
se = pop_std / np.sqrt(sample_n)

# 95%置信区间
CI_debt = stats.norm.interval(confidence, loc=sample_mean, scale=se)

# %%
# 总体均值的区间估计：小样本
s_sample = np.random.randint(1, 400, 15)
confidence = 0.95
sample_n = len(s_sample)

# 抽样平均误差
se = s_sample.std() / np.sqrt(sample_n)

# 样本均值
sample_mean = s_sample.mean()

# %%
# 95%置信区间
CI_debt = stats.t.interval(confidence, df=sample_n - 1, loc=sample_mean, scale=se)

print('点估计值为', sample_mean)
print('95%置信区间为', CI_debt)

# %%
# 实验4-3 总体比例的估计

"""
要估计一批总数为5000件的产品的废品率，于是抽出400件产品进行检测，
发现32件废品。试给出该批产品的废品率的区间估计（置信度90%）
"""
confidence = 0.9
n = 5000  # 整体数据
sample_n = 400
sample_reject = 32
sample_p = sample_reject / sample_n

sigma_reject = np.sqrt(((sample_p * (1 - sample_p)) / sample_n) * ((n - sample_n) / (n - 1)))

print('点估计值为', sample_p)
CI_reject_rate = stats.norm.interval(confidence, sample_p, sigma_reject)
# %%
# 总体方差的估计
"""
某种药物，18个样本得出的样本方差是0.36克。
构造该药物方差的90%置信区间概率。假设药物重量服从正态分布
"""
confidence = 0.90
sample_n = 18
sample_var = 0.36

# 计算卡方分布
chi2_lower, chi2_higher = stats.chi2.interval(confidence, sample_n)

# 计算(n-1)*样本方差的值
sample_df_var = (sample_n - 1) * sample_var

# 计算得到总体方差的置信区间估计
CI_weight_var = (sample_df_var / chi2_higher, sample_df_var / chi2_lower)
print(CI_weight_var)

# %%
# 第二节 参数检验
# 实验4-5 单一总体均值检验：大样本

"""
一种减肥法称一星期平均减肥3.5公斤。40个用此法的个人组成一个随机样本，
称减去的体重的样本均值为3公斤，
样本标准差为1.5公斤。该如何对该减肥方法做出判断？（显著性水平0.05）
"""
"""
H0:μ>=3.5
H1:μ<3.5
"""
confidence = 0.05
sample_n = 40
sample_mean = 3
sample_std = 1.5
test_mean = 3.5

# 计算5%显著水平的正态分布临界值（左侧检验）
left_limit = stats.norm.ppf(confidence)

# 计算检验统计量
z = (sample_mean - test_mean) / (sample_std / np.sqrt(sample_n))

print('临界值为', left_limit)
print('检验统计量为', z)

"""
由于 检验统计量的值为 -2.1081851067789197 小于 临界值为 -1.6448536269514729
因此拒绝原假设，即该减肥法自称平均减少3.5公斤是不真实的
"""
# %%
# 实验4-7 单一总体均值检验：正态总体，方差未知
"""
厂子生产糖果，标准是每袋净重500克，现在从一批生产中抽出10袋，净重分别如下。
给定显著性水平0.01，问该批生产是否正常。假设糖果重量符合正态分布。
H0:μ=500
H1:μ不等于500
使用t检验
"""

sample = [512, 503, 498, 507, 496, 489, 499, 501, 496, 506]
confidence = 0.01
test_mean = 500

# 方法1,比较p值和置信度
results = stats.ttest_1samp(sample, popmean=test_mean)
print('检验样本统计量t为', results[0])
print('p值为', results[1])

# 方法二 计算t再计算临界值判断
results = stats.ttest_1samp(sample, popmean=test_mean)
limit = stats.t.ppf(confidence / 2, df=len(sample) - 1)
print('检验样本统计量t为', results[0])
print('t临界值为（双侧检验）', limit, '和', -limit)

# 方法三 使用公式计算t统计量，比较临界值
t = (np.mean(sample) - test_mean) / (np.std(sample) / np.sqrt(len(sample)))
limit = stats.t.ppf(confidence / 2, df=len(sample) - 1)
print('t统计量为', t)
print('t临界值为(双侧检验)', -limit, '和', limit)

"""
结论
从p值看，p=0.7450329 > 0.01，因此1%abs显著性水平下不能拒绝原假设，可认为该批次生产正常
从临界值看，因为 -3.24983554401537<0.335367<3.24983554401537，也可以说明不能拒绝原假设，
该批次生产正常
"""
# %%
# 实验4-8 两个总体的均值检验：总体方差未知，大样本
"""
一次大型考试，检测男女生差异。假设这些男女生数学成绩相同，562名女生和852名男生。
他们的词汇得分如下：女生平均分547，样本标准差83；男生平均分525，样本标准差78
问，数学成绩相同的女生总体和男生总体，女生词汇能力是否明显高于男生？显著性水平=0.01
H0:μ1 - μ2 <= 0
H1:μ1 - μ2 > 0
假设两总体服从正态分布，由于总体方差未知，但样本容量较大，所以使用Z检验统计量。
"""

confidence = 0.01
sample_n1 = 562
sample_mean1 = 547
sample_std1 = 83

sample_n2 = 852
sample_mean2 = 525
sample_std2 = 78
z = (sample_mean1 - sample_mean2) / (np.sqrt(sample_std1 ** 2 / sample_n1 + sample_std2 ** 2 / sample_n2))

# 临界值（右侧检验）
limit = stats.norm.ppf(1 - confidence)
print('z统计量为', z)
print('正态临界值(右侧检验)为', limit)

"""
结论
由于z = 4.9949904689768685 > 临界值 2.3263478740408408
因此拒绝原假设，接受备择假设。也就是说女生词汇能力的确明显高于男生
"""

# %%
# 实验4-9 两独立样本t检验
"""
12名会计师和14名财务人员起始年薪如下。
在显著性水平=0.05下，检验两种职业起始年薪有无差异。
H0:μ1 - μ2 = 0
H1:μ1 - μ2 不等于 0
假设两总体服从正态分布。
总体均值在小样本下的检验是在两总体服从正态分布假定下进行的，与大样本下的检验方法基本相同。
不同的是，需要区分总体方差已知和总体方差未知两种情况。
"""
job = {
    "会计师":  [30.6, 31.2, 28.9, 35.2, 25.1, 33.2, 31.3, 35.3, 31.0, 30.1, 29.9, 24.4, np.nan, np.nan],
    '财务人员': [31.6, 26.6, 25.5, 25.0, 25.9, 32.9, 26.9, 25.8, 27.5, 29.6, 23.9, 26.9, 24.4, 25.5]
}
df = pd.DataFrame(job)
series1 = df['会计师'].dropna()
series2 = df['财务人员'].dropna()

# 情况1,总体方差未知但相等
results = stats.ttest_ind(series1, series2, equal_var=True)
print('t统计量为', results[0])
print('p值为:', results[1])

# 情况二，总体方差未知且不相等
results = stats.ttest_ind(series1, series2, equal_var=False)
print('t统计量为', results[0])
print('p值为:', results[1])

# %%
# 实验4-10 配对样本t检验
"""
消费者给商品打分0~10分，分越高表示购买潜力越高。看广告前后各打一次分。
显著性水平=0.05 根据样本数据判断广告是否提高了平均购买力
H0:μ1 - μ2 = 0
H1:μ1 - μ2 不等于 0
"""
data = {
    '看广告之后': [6, 6, 7, 4, 3, 9, 7, 6],
    '看广告之前': [5, 4, 7, 3, 5, 8, 5, 6]
}
df = pd.DataFrame(data)
ad_after = df['看广告之后']
ad_before = df['看广告之前']

# 方案1
results = stats.ttest_rel(ad_after, ad_before)
print('t统计量为', results[0])
print('p值为:', results[1])
"""
p = 0.2168375456189006 > 0.05,所以不能拒绝原假设，因而广告没有使潜在购买力提高
"""
# 方案2
confidence = 0.05
results = stats.ttest_rel(ad_before, ad_after)
# 计算临界值（双侧检验）
limit = stats.t.ppf(1 - confidence / 2, df=(len(df) - 1))
print('t统计量为', results[0])
print('临界值为', limit)
"""
t = 1.3572417850765923 < 临界值 = 2.3646242510102993，
因此，接受原假设，即广告没有使潜在购买力提高
"""

# %%
# 实验4-11 单一总体比例的假设检验
"""
快餐店有种特殊饮料，如果15%的顾客买它，则认为可以提供这种特殊供应。初步实验表明，
500名顾客中88人买了。请问是否提供这种特殊饮料的供应？
显著性水平 = 0.01
H0:ρ>=15%
H1:ρ<15%
大样本下，无论总体是否服从正态分布，样本成数近似服从正态分布，因此选择Z检验统计量。
"""

confidence = 0.05
sample_n = 500
sample_buyer = 88
sample_p = sample_buyer / sample_n
test_p = 0.15

# 计算临界值
limit = stats.norm.ppf(confidence)

# 计算检验统计量
z = (sample_p - test_p) / np.sqrt(test_p * (1 - test_p) / sample_n)
print('临界值为', limit)
print('检验统计量为', z)

# %%
# 实验4-12 两个总体的成数检验
"""
对600人进行一项调查，其中300名女性中279人同意；300名男性中255名同意
显著性水平=0.05，问这一调查，男女的同意比例是否相同
大样本比例均服从正态分布，因此两样本比例之差也服从正态分布，选择Z统计量。
"""
confidence = 0.05
female_n = 300
female_agree = 279
p1 = female_agree / female_n

male_n = 300
male_agree = 255
p2 = male_agree / male_n

limit = stats.norm.ppf(confidence / 2)

# 计算检验统计量公式中的P
z_p = (female_n * p1 + male_n * p2) / (female_n + male_n)

# 计算统计检验量z
z = (p1 - p2) / np.sqrt(z_p * (1 - z_p) * (1 / female_n + 1 / male_n))

print('成数P为', z_p)
print('t临界值为', limit, '和', -limit)
print('检验统计量为', z)

"""
检验统计量为 3.131441267637955 > 1.9599639845400545，拒绝原假设，即表明男女是否同意有明显不同
"""

# %%
# 实验4-13 单一总体方差的假设检验
"""
杂志A订阅者中拥有车的数量的方差为0.94，杂志B的订阅者中选12个样本，其拥有车的数量如下。
假设两种杂志订阅者拥有车的数量的方差相同。显著性水平=0.05
H0:sigma^2 = 0.94
H1:sigma^2 不等于 0.94
用卡方作为检验统计量
"""
car = [2, 1, 2, 0, 3, 2, 2, 1, 2, 1, 0, 1]

confidence = 0.05
teset_var = 0.94

# 计算临界值
limit = stats.chi2.ppf(confidence, df=(len(car)) - 1)
limit_lower, limit_higher = stats.chi2.interval(1 - confidence, df=(len(car) - 1))
