import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

"""
单变量线性回归实现
    笔记: 对于np.array或np.ndarray:
            A * x = 按位相乘
            A.dot(x) = 矩阵乘法
          对于np.matrix
            A * x = 矩阵乘法
        ======================================
        (97,1)是列向量(二位数组)。而(97,)只是一维数组,而且它也不能转置(T)成列向量
        
"""
class LinearRegression(object):

    def __init__(self, data: DataFrame) -> None:
        super().__init__()
        # 特征缩放
        data = (data - data.mean()) / data.std()
        # draw_raw_data(data)
        # 插入一列来x₀方便向量化计算
        data.insert(0, 'Ones', 1)
        cols = data.shape[1]  # 获取数据的总列数
        X = data.iloc[:, 0:cols - 1]  # X是所有行，去掉最后一列
        y = data.iloc[:, cols - 1:cols]  # y是所有行的最后一列
        X = np.array(X.values)  # (m * n)
        y = np.array(y.values)  # (m * 1)
        # 列向量 (n * 1)
        theta = np.array([[x for x in range(X.shape[1])]], dtype=float).T
        print(self.compute_cost_d(X, y, theta))
        goal, costs = self.gradient_decent(X, y, theta, alpha=0.01, iter_num=1000)
        if data.shape[1] < 3:
            draw_h(data, goal)
        self.draw_cost(costs)


    def h(self, X: np.ndarray, theta):
        """
        猜测函数 线性函数
        :param X: 样本特征矩阵 行代表每个样本实例 列代表样本特征 (m * n)
        :param theta: 参数 列向量 (n * 1)
        :return: 猜测函数的输出 列向量 (m * 1)
        """
        return X.dot(theta)

    def compute_cost(self, X, y, theta):
        """
        代价函数
        :param X: 样本特征矩阵 行代表每个样本实例 列代表样本特征 (m * n)
        :param y: 标签 列向量 (m * 1)
        :param theta: 参数 列向量 (n * 1)
        :return:
        """
        inner = np.power((self.h(X, theta) - y), 2)
        return np.sum(inner) / (2 * len(X))

    def compute_cost_d(self, X, y, theta):
        """
        代价函数的导数, 返回(1 * n)
        :param X: 样本特征矩阵 行代表每个样本实例 列代表样本特征 (m * n)
        :param y: 标签 列向量 (m * 1)
        :param theta: 参数 行向量 (1 * m)
        :return: 每个样本特征的偏导数 行向量 (1 * n)
        """
        #    (1 * m) * (m * n) = (1 * n)
        return ((self.h(X, theta) - y).T.dot(X)) / len(X)

    def gradient_decent(self, X, y, theta, alpha=0.01, iter_num=1000):
        """
        梯度下降算法
        :param X: 样本特征矩阵 行代表每个样本实例 列代表样本特征 (m * n)
        :param y: 标签 列向量 (m * 1)
        :param theta: 参数 行向量 (1 * n)
        :param alpha: 学习速率
        :param iter_num: 梯度下降次数
        :return: 梯度下降后theta的最终值(n * 1) 与 每次迭代后的代价
        """
        costs = np.zeros(iter_num)
        for iter in range(iter_num):
            theta -= alpha * self.compute_cost_d(X, y, theta).T
            cost = self.compute_cost(X, y, theta)
            costs[iter] = cost
            print(f'第{iter}次梯度下降, 代价cost:{cost}')
        return theta.T, costs

    def draw_cost(self, costs):
        """
        绘制代价曲线
        :param costs:
        :return:
        """
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.plot(np.arange(len(costs)), costs, 'r')
        ax.set_xlabel('Iterations')
        ax.set_ylabel('Cost')
        ax.set_title('Error vs. Training Epoch')
        plt.show()


def draw_raw_data(data: DataFrame):
    """
    绘制原生的数据点图像
    """
    data.plot(kind='scatter', x='Population', y='Profit', figsize=(12, 8))
    plt.show()


def draw_h(data: DataFrame, goal: np.ndarray):
    """
    绘制最终的猜测函数图像
    """
    x = np.linspace(data.Population.min(), data.Population.max(), 100)
    f = goal[0][0] + (goal[0][1] * x)
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(x, f.T, 'r', label='Prediction')
    ax.scatter(data.Population, data.Profit, label='Traning Data')
    ax.legend(loc=2)
    ax.set_xlabel('Population')
    ax.set_ylabel('Profit')
    ax.set_title('Predicted Profit vs. Population Size')
    plt.show()


def deal_ex1():
    path = 'ex1data1.txt'
    data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
    LinearRegression(data)


def deal_ex2():
    path = 'ex1data2.txt'
    data = pd.read_csv(path, header=None, names=['Size', 'RoomNum', 'Price'])
    LinearRegression(data)


if __name__ == '__main__':
    deal_ex1()
    # deal_ex2()
