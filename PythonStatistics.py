import math
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
import itertools


#https://stackoverflow.com/questions/27928275/find-p-value-significance-in-scikit-learn-linearregression
def RegressionResult(x,y):
        x2 = sm.add_constant(x);
        est = sm.OLS(y, x2).fit();
        pArr = [est.pvalues[i] for i in range(len(x[0]))]
        ans = (str(est.summary()), pArr, est.params.tolist());
        return ans;

def makeFactorsMatrix(name, factors):
        ii = 0;
        numF = len(factors);
        numFm = 1+ numF + numF + int(math.factorial(numF)/2);   #1, x1^2, x1, x1*x2
        matrixF = np.zeros(numFm);
        matrixN = ["" for _ in range(numFm)]
        matrixF[0] = 1; # const
        matrixN[0] = "const";
        combinationF = itertools.combinations(factors,2);
        combinationN = itertools.combinations(name,2);
        for i in range(numF):
                matrixF[1+i] = factors[i];
                matrixN[1+i] = name[i];
                matrixF[numF+1+i] = factors[i]**2;
                matrixN[numF+1+i] = name[i] + "^2";
        for i in combinationF:
                matrixF[numF*2+1+ii] = i[0] * i[1];
                ii+=1;
        ii=0;
        for i in combinationN:
                matrixN[numF*2+1+ii] = i[0] + "*" + i[1];
                ii+=1;        
        return (matrixF.tolist(), matrixN)
        
