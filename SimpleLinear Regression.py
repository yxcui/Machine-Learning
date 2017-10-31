# -*- coding:utf-8 -*-
import numpy as np

def fitSLR(x, y):  # x,y分别为自变量和因变量的样本值
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = 0  # 分子
    dinominator = 0  # 分母
    for i in range(0,n):
        numerator += (x[i] - x_mean)*(y[i] - y_mean)
        dinominator += (x[i] - x_mean)**2
    b1 = numerator/float(dinominator)
    b0 = y_mean - b1*float(x_mean)
    print "b0: %f, b1: %f" %(b0,b1)
    return b0,b1

def predict(x,b0,b1):
    return b0 + b1*x

if __name__ == "__main__":
    x = [1,3,2,1,3]
    y = [14,24,18,17,27]
    b0,b1 = fitSLR(x,y)
    print "intercept: %f, slope:%f" %(b0,b1)

    x_test = 6
    y_test = predict(x_test,b0,b1)
    print "The linear regression equation is y = %f + %f x" %(b0, b1)
    print "y_test:", y_test
