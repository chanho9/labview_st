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
        return (matrixF.tolist(), matrixN);


## basic statistics...

def stdvar(arr):
        ans1 = np.mean(arr);
        ans2 = np.std(arr);
        ans3 = np.var(arr);
        return (ans1, ans2, ans3);

#나중에 받는 타입에 상관없이 동작하게 변경
#https://medium.com/human-in-a-machine-world/mae-and-rmse-which-metric-is-better-e60ac3bde13d
#https://mechamath.tistory.com/entry/4-%EC%98%A4%EC%B0%A8Error
def errCal(typeIndex, predictions, targets):
        ans1=0;
        ans2=np.array([0,0]);
        predictions = np.array(predictions)
        targets = np.array(targets)
        if typeIndex==0: # Root mean squared error
                ans1 = np.sqrt(((predictions - targets) ** 2).mean());
        elif typeIndex==1: # Mean Absolute Error
                ans1 = ((predictions - targets) ** 2).mean();
        elif typeIndex==2: # Relative True Error + RMSE
                ans1= np.sqrt(((predictions - targets)/targets ** 2).mean());
        elif typeIndex==3: # Approximate error
                ans1 = abs((predictions[-1]-predictions[-2])/predictions[-1])
                ans2 = (predictions[:-1]-predictions[1:])/predictions[1:];
                ans2 = np.array([abs(number) for number in ans2]);
        else:
                pass;
        return (ans1, ans2.tolist())

def covariance(x):
        ans1 = np.cov(x);
        ans2 = [np.mean(row) for row in x]
        return (ans1.tolist(), ans2);

def correlationCoef(x,y):
        x = np.array(x);
        y = np.array(y);
        ans = np.corrcoef(x,y);
        return ans.tolist();

# 정규성 검정
# https://namyoungkim.github.io/statistics/2017/09/14/probability/
# https://rfriend.tistory.com/tag/%EB%8B%A8%EC%9D%BC%20%EB%AA%A8%EC%A7%91%EB%8B%A8%20%EB%B6%84%ED%8F%AC%EC%9D%98%20%EC%A0%95%EA%B7%9C%EC%84%B1%20%EA%B2%80%EC%A0%95
                
