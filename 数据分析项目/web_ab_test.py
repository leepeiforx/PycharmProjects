import pandas as pd
import common.utils as utils

# %%

file_path = r'数据分析项目/date_file/ab_data.csv'

df = pd.read_csv(file_path)
# print(df.head())
print(utils.show_na(df))  # 检查NA值
print(utils.show_info(df))  # 检查数据极值
print(utils.show_duplicated(df))  # 检查重复值情况

# %%
# 新旧页面转化率
control_isconverted_num = df[
    (df['landing_page'] == 'old_page') & (df['converted'] == 1) & (df['group'] == 'control')]['user_id'].nunique()
control_view_num = df[(df['landing_page'] == 'old_page') & (df['group'] == 'control')]['user_id'].count()
control_tr = round((control_isconverted_num * 100 / control_view_num), 4)

control = {
    '转换数': control_isconverted_num,
    '浏览数': control_view_num,
    '转化率': str(control_tr) + '%'
}

treatment_isconverted_num = df[
    (df['landing_page'] == 'new_page') & (df['converted'] == 1) & (df['group'] == 'treatment')]['user_id'].nunique()

treatment_view_num = df[(df['landing_page'] == 'new_page') & (df['group'] == 'treatment')]['user_id'].count()

treatment_tr = round((treatment_isconverted_num * 100 / treatment_view_num), 4)
treatment = {
    '转换数': treatment_isconverted_num,
    '浏览数': treatment_view_num,
    '转化率': str(treatment_tr) + '%'
}

print('控制组', control)
print('实验组', treatment)

'''
从该结果来看，在本数据集中新旧页面的转换率具有明显差异，改版后的页面在一定程度上显著提高了用户的转换
下一步，用假设检验来验证此猜想：旧页面的转换率低于新页面的转换率
'''

# %%
# 2假设验证
"""
从控制组和实验组中各抽取一定数量的样本来进行假设检验，设旧页面的转换率为P0，新页面的转换率为P₁，则：
原假设H0： P0 ≤P₁
备则假设H₁：P₁ >P0
置信水平 α 的选择经验
    样本量      α-level  
    ≤100        10%  
    100＜n≤500   5%  
    500＜n≤1000  1%  
    n＞2000     千分之一  
样本量过大，α-level 就没什么意义了。使用分层抽样，定义一个函数：
"""


def get_sample(df, sampling='simple_random', k=1, stratified_col=None):
    """
    :param df: 输入的数据框pandas.DataFrame对象
    :param sampling:抽样方法 str
    可选值有['simple_random','stratified','systematic']
    :param k:抽样个数或抽样比例 int or float
            (int, 则必须大于0; float, 则必须在区间(0,1)中)
            如果 0 < k < 1 , 则 k 表示抽样对于总体的比例
            如果 k >= 1 , 则 k 表示抽样的个数；当为分层抽样时，代表每层的样本量
    :param stratified_col:需要分层的列名的列表 list 只有在分层抽样时才生效
    :return: 抽样结果,返回数据框pandas.DataFrame对象
    """

    import random
    from functools import reduce
    import numpy as np
    import math

    len_df = len(df)
    if k <= 0:
        raise AssertionError('k不能为负数')
    elif k > 1:
        assert isinstance(k, int), '选择抽样个数时,k必须为正整数'
        sample_by_n = True
        if sampling == 'stratified':
            alln = k * df.groupby(stratified_col)[stratified_col[0]].count().count()
            if alln >= len_df:
                raise AssertionError('请确认k乘以层数不能超过总样本量')
    else:
        sample_by_n = False
        if sampling in ('simple_random', 'systematic'):
            k = math.ceil(len_df * k)

    if sampling == 'simple_random':
        print('使用简单随机抽样')
        idx = random.sample(range(len_df), k)
        res_df = df.iloc[idx, :].copy()
        return res_df

    elif sampling == 'systematic':
        print('使用系统抽样')
        step = len_df // k + 1
        start = 0
        idx = range(len_df)[start::step]
        res_df = df.iloc[idx, :].copy()
        return res_df

    elif sampling == 'stratified':
        #         设置断言
        assert stratified_col is not None, '请传入包含分层所需要的列名的列表'
        assert all(np.in1d(stratified_col, df.columns)), '检查输入的列名'
        grouped = df.groupby(by=stratified_col)[stratified_col[0]].count()
        if sample_by_n:
            group_k = grouped.map(lambda x: k)
        else:
            group_k = grouped.map(lambda x: math.ceil(x * k))

        res_df = pd.DataFrame(columns=df.columns)
        for df_idx in group_k.index:
            df1 = df
            if len(stratified_col) == 1:
                df1 = df1[df1[stratified_col[0]] == df_idx]
            else:
                for i in range(len(df_idx)):
                    df1 = df1[df1[stratified_col[i]] == df_idx[i]]
            idx = random.sample(range(len(df1)), group_k[df_idx])
            group_df = df1.iloc[idx, :].copy()
            res_df = res_df.append(group_df)
        return res_df
    else:
        raise AssertionError("sampling is illegal")


data = get_sample(df, sampling='stratified', stratified_col=['group'], k=300)

# 新旧版本转换数
control_isconverted_num = data[
    (data['landing_page'] == 'old_page') & (data['converted'] == 1) & (data['group'] == 'control')]['user_id'].nunique()
control_view_num = data[(data['landing_page'] == 'old_page') & (data['group'] == 'control')]['user_id'].count()

# 新旧版本浏览数
treatment_isconverted_num = data[
    (data['landing_page'] == 'new_page') & (data['converted'] == 1) & (data['group'] == 'treatment')][
    'user_id'].nunique()
treatment_view_num = data[(data['landing_page'] == 'new_page') & (data['group'] == 'treatment')]['user_id'].count()

# 新旧版本标准差
control_std = data[(data['landing_page'] == 'old_page')]['converted'].std()
treatment_std = data[(data['landing_page'] == 'new_page')]['converted'].std()

print(control_std, treatment_std)

# %%
# z,p值计算
import statsmodels.stats.proportion as sp

z_score, p_value = sp.proportions_ztest([control_isconverted_num, treatment_isconverted_num],
                                        [control_view_num, treatment_view_num], alternative='smaller')
print(z_score, p_value)