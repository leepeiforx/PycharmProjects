import numpy as np

# 待降维的数据
a = np.array([[3, 2, 4, 5, 1], [2000, 3000, 5000, 8000, 2000]])
a = a.T

# 使用numpy模拟PCA计算过程
# 数据归一化
mean = np.mean(a, axis=0)
norm = a - mean
scope = np.max(a, axis=0) - np.min(a, axis=0)
norm = norm / scope

# %%
U, S, V = np.linalg.svd(np.dot(norm.T, norm))

U_reduce = U[:, 0].reshape(2, 1)
print(U)
print(U_reduce)

# 降维
print('\n')
R = np.dot(norm, U_reduce)
print(R)

# 还原
Z = np.dot(R, U_reduce.T)

# 数据还原(做数据预处理的逆运算)
Z = np.multiply(Z, scope) + mean

print(Z)

# %%
# 使用sklearn进行PCA降维
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler


def std_PCA(**kwargs):
    scaler = MinMaxScaler()
    pca = PCA(**kwargs)
    pipline = Pipeline([('scaler', scaler), ('pca', pca)])
    return pipline


pca = std_PCA(n_components=1)
r2 = pca.fit_transform(a)
pca.inverse_transform(r2)
