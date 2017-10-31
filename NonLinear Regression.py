# -*- coding:utf-8 -*-
import numpy as np
import random
import time
## 用来产生随机数矩阵的
def genData(numSamples, bias, variance):
    x = np.zeros(shape=(numSamples, 2))  # 实例矩阵初始化(numSamples个实例，2个变量)
    y = np.zeros(shape=numSamples)  # 存储label列(1)，这是向量
    for i in range(0,numSamples):
        x[i][0] = 1
        x[i][1] = i
        y[i] = (i + bias) + random.uniform(0, 1) * variance  # 产生随机数
    return x, y
## 梯度下降算法，这是一个通用算法，通过更新法则求偏导，找到最低点
def gradientDescent(x, y, theta, alpha, m, numIterations):  # theta是最终要学习的参数值(一个向量)，即待求解，alpha是学习率
    xTrans = x.transpose()  # 用于矩阵运算
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta)  # 用于求解内积，即为模型的向量表示，结果即为预测值
        loss = hypothesis - y  # 误差项
        cost = np.sum(loss**2)/(2*m)  # 定义一个Cost函数，cost越小越好
        print "Iteration %d | Cost: %f" % (i, cost)  # 查看每一步的cost是否在减小？
        gradient = np.dot(xTrans, loss) / m  # 更新量（来自更新法则）
        theta = theta - alpha * gradient
        # time.sleep(1)
    return theta
if __name__ == "__main__":
    x, y = genData(100, 25, 10)
    print x
    print y
    m, n = np.shape(x)
    numIterations = 200000
    alpha = 0.0005  # 在0-1之间，一般alpha可以动态调整，但是如果太大，容易跳过local minimum，太小影响执行效率
    theta = np.ones(n)  # 维度根据参数的个数设置
    theta = gradientDescent(x, y, theta, alpha, m, numIterations)
    print theta
