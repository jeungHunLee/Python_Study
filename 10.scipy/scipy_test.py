# scipy
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.linalg import *
from scipy.optimize import *
from scipy.integrate import quad
from scipy.stats import linregress

# 연립 방정식
a = np.array([[3, 2, 0],
             [1, -1, 0],
             [0, 5, 1]])
b = np.array([2, 4, -1])
s = solve(a, b)    # 연립 방정식 계산
print(f'(x, y, z) = {s}')    # (x, y, z) = [ 2. -2.  9.]

# 비선형 방정식의 해
x = np.linspace(-1, 1, 101)
plt.plot(x, np.exp(-x))
plt.plot(x, x)
plt.show()

def f(x):
    return x - math.exp(-x)

print(fsolve(f, 0.5))

# 함수의 최솟값
def f(x):
    return x ** 2 + 10 * np.sin(x)

x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x))
plt.show()

print(fmin_bfgs(f, 0))    # 0에서 시작해서 탐색
print(fmin_bfgs(f, 6))    # 6에서 시작해서 탐색

# 수치적분
def f1(x): return x ** 2
def f2(x): return np.exp(-x)

x = np.arange(0, 100)
plt.plot(x, f1(x))
plt.plot(x, f2(x))
plt.show()

print(quad(f1, 0, 1))    # (0.3333333333333333, 3.700743415417188e-15)
print(quad(f2, 0, np.inf))    # (1.0, 5.842605965544164e-11)

# 선형 회귀
x = np.linspace(0, 10, 5)
y = [1.5, 3.1, 4.2, 5.8, 7.3]

slope, intercept, r_value, p_value, std_err = linregress(x, y)
'''
slope: 기울기
intercept: 절편
r_value: 상관계수
p_vluae: 예측 불확실성
std_err: 표준편차
'''
print(f'slope = {slope:.3f}')    # slope = 1.907
print(f'intercept = {intercept:.3f}')    # intercept = 1.520

yfit = slope * x + intercept

plt.plot(x, y, 'o', label='data')
plt.plot(x, yfit, 'r', label='fitting line')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 비선형 회귀
def func(x, a, b, c):
    return a * x + b * np.exp(-c * x ** 2)

x = np.linspace(-5, 5, 101)
y = 0.6 * x + 5 * np.exp(-0.2 * x ** 2) + np.random.rand(101)

popt, pcov = curve_fit(func, x, y)
print(popt)    # [0.58163607 5.35975701 0.14709613]

yfit = func(x, *popt)

plt.plot(x, y, 'o', label='data')
plt.plot(x, yfit, 'r', label='fitting curve')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

