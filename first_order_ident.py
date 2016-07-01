# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 11:04:35 2016

@author: Baptiste Marechal
"""

from scipy import signal, linspace, pi, randn, ones
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import time

tic = time.time()

'''function to optimize'''
def func(u, K, tau, y0):
    sys = signal.lti(K, [tau, 1])
    y = sys.output(u, t, y0)
    return y[1]

'''input square signal'''
global t
t = linspace(0, 20, 1000)
Umes = -0.5*(signal.square(2*pi*0.1*t)+ones(len(t)))+ones(len(t))+randn(len(t))/50

'''noisy output signal'''
p = [1, 1, 0]
Ymes = func(Umes, *p)+randn(len(Umes))/50

'''input and output signals plot'''
plt.plot(t, Umes, label = 'Umes')
plt.plot(t, Ymes, label = 'Ymes')


'''optimization with non-linear least squares method'''
popt, cov = curve_fit(func, Umes, Ymes)
print(p)
print(popt)

'''estimated response plot'''
Yfit = func(Umes, *popt)
plt.plot(t, Yfit, label ='Yfit')

plt.legend()
plt.grid()
plt.show()

toc = time.time() - tic
print(toc)