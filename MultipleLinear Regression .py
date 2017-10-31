# -*- coding:utf-8 -*-
from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model

dataPath = r"Delivery.csv"
deliveryData = genfromtxt(dataPath, delimiter=',')  # 因为是csv格式，即为','分隔
print "data: ", deliveryData

X = deliveryData[:, :-1]
Y = deliveryData[:, -1]
print "X: ", X
print "Y: ", Y

regr = linear_model.LinearRegression()
regr.fit(X,Y)
print "coefficients:%f, intercept:%f" % (regr.coef_, regr.intercept_)

xPred = [102, 6]
yPred = regr.predict(xPred)
print "yPred:%f" % yPred

