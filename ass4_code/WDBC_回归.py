# 随机森林算法
# 数据集：wdbc,iris
"""
回归任务：忽略两个数据集中的类别属性，从其余属性中任选一个作为回归任务的目标属性；
分别对两个数据集按照自行设定的比例进行训练集、测试集的划分，
使用训练集分别训练随机森林跟AdaBoost回归器，并分别用测试集测试其性能。
"""
# SONG
# 2023/5/9

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, explained_variance_score, median_absolute_error
from sklearn.ensemble import RandomForestRegressor

# 加载数据集
names = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
         'compactness_mean', 'concavity_mean', 'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
         'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se',
         'concave_points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst',
         'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst',
         'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst']
data = pd.read_csv('../dataset/wdbc/wdbc.data', names=names)


# 分离特征和标签
X = data.drop(['id', 'diagnosis','fractal_dimension_worst'], axis=1)
y = data['fractal_dimension_worst']

# 将数据集划分为训练集和测试集
X_trainval, X_test, y_trainval, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

######################################### 随机森林回归器 ######################################################

# 构建随机森林回归器
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# 训练模型
rf_regressor.fit(X_trainval, y_trainval)

# 预测测试集结果
y_pred = rf_regressor.predict(X_test)


print("随机森林算法")
# 计算均方误差（MSE）
mse = np.mean((y_test - y_pred) ** 2)
print('均方误差（MSE）:', mse)

# 计算平均绝对误差（MAE）
mae = mean_absolute_error(y_test, y_pred)
print('平均绝对误差（MAE）:', mae)

# 计算决定系数（R²）
r2 = r2_score(y_test, y_pred)
print('决定系数（R²）:', r2)

# 计算解释方差分数
evs = explained_variance_score(y_test, y_pred)
print('解释方差分数:', evs)

# 计算中位绝对误差
medae = median_absolute_error(y_test, y_pred)
print('中位绝对误差（MedAE）:', medae)

