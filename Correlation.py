# -*- coding:utf-8 -*-
import numpy as np
from astropy.units import Ybarn
import math 

def computeCor(X, Y):
    xBar = np.mean(X)
    yBar = np.mean(Y)
    Cov = 0
    xVar = 0
    yVar = 0
    for i in range(0, len(X)):
        diffXXBar = X[i] - xBar
        diffYYBar = Y[i] - yBar
        Cov += diffXXBar * diffYYBar
        xVar += diffXXBar**2
        yVar += diffYYBar**2

    xyVar = math.sqrt(xVar * yVar)
    return Cov / xyVar

## Polynomial Regression
def polyfit(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    # Coefficients
    results['polynomial'] = coeffs.tolist()
    # R_squared
    predict = np.poly1d(coeffs)
    # fit value and mean
    yHat = predict(x)
    yBar = np.sum(y)/len(y)
    SSr = np.sum((yHat - yBar)**2)
    SSt = np.sum((y - yBar)**2)

    results['determination'] = SSr / SSt
    return results

if __name__ == "__main__":
    testX = [1, 3, 8, 7, 9]
    testY = [10, 12, 24, 21, 34]
    r = computeCor(testX, testY)
    print r
    R_square = polyfit(testX, testY, 1)
    print R_square
