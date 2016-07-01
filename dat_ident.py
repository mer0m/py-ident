# -*- coding: utf-8 -*-

import csv, time, glob, datetime, os
import matplotlib.pyplot as plt
import matplotlib.dates as md

#from scipy import signal
#from scipy.optimize import curve_fit

tic = time.time()

os.chdir('/home/user/sicav_data/Manip/2016/2016-03/')

def getColumn(filename, column):
    results = []
    for dat_file in sorted(glob.glob(filename)):
        file_result = csv.reader(open(dat_file), delimiter='\t')
        results = results + map(float,[result[column] for result in file_result])
    return results

t = getColumn('*-lakeshore.dat', 0)
T1 = getColumn('*-lakeshore.dat', 2)
T2 = getColumn('*-lakeshore.dat', 3)
T3 = getColumn('*-lakeshore.dat', 4)
T4 = getColumn('*-lakeshore.dat', 5)

"""
n = 400
t = [t[n*i] for i in range(len(t)/n)]
T1 = [T1[n*i] for i in range(len(T1)/n)]
T2 = [T2[n*i] for i in range(len(T2)/n)]
T3 = [T3[n*i] for i in range(len(T3)/n)]
T4 = [T4[n*i] for i in range(len(T4)/n)]

def func(U, a0, b1, b2, y0):
    sys = signal.lti([a0],[b2, b1, 1])
    y = sys.output(U, t, y0)
    return y[1]

print('Fitting...')
popt, cov = curve_fit(func, T1, T4)
print(popt)
Yfit = func(T1, *popt)
"""
timetamps = [datetime.datetime.fromtimestamp(ti) for ti in t]
datenums=md.date2num(timetamps)

plt.subplots_adjust(bottom=0.35)
plt.xticks(rotation=90)
ax=plt.gca()
xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)

plt.plot(datenums, T1, label = 'Table')
plt.plot(datenums, T2, label = 'Link st.')
plt.plot(datenums, T3, label = 'PT2')
plt.plot(datenums, T4, label = 'Reg. st.')
#plt.plot(datenums, Yfit, label = 'Fit')

plt.legend()
plt.grid()
plt.show()

toc = time.time() - tic
print(toc)
