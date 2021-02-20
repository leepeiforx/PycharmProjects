import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt

n_dots = 40
X = 5 * np.random.randn(n_dots, 1)
y = np.cos(X).ravel()

# 加入噪音
y += 0.2 * np.random.rand(n_dots) - 0.1

# 训练模型
k = 5
knn = KNeighborsRegressor(k)
knn.fit(X, y)

# 生成足够密集的点并进行预测
T = np.linspace(0, 5, 500).reshape(-1, 1)
y_pred = knn.predict(T)
knn.score(X, y)

# 画出拟合曲线
plt.figure(figsize=(16, 10), dpi=200)
plt.scatter(X, y, c='g', label='data', s=100)
plt.plot(T, y_pred, c='k', label='prediction', lw=4)
plt.xticks()
plt.xlim(0, 10)
plt.axis('tight')
plt.title('KNeighborsRegressor(k={})'.format(k))
plt.show()
