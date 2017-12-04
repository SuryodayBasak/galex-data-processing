import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde
from scipy.stats import norm
from numpy import linspace,hstack
from pylab import plot,show,hist
import numpy as np

df = pd.read_csv('hist_a_specter_python.csv')

features_list = ['x','y']
count = 0

x0 = []
y0 = []
x1 = list(df['x'])
y1 = list(df['y'])
x2 = []
y2 = []

"""
for i in range(len(x1)):
	if y1[i] != 0:
		x0.append(x1[i])
		y0.append(np.log(y1[i]))
		#print(x1[i], y2[i])
plt.plot(x0,y0)
"""

for i in range(len(x1)):
#for i in range(150):
	if y1[i] != 0:
		x2.append(x1[i])
		y2.append(np.log(y1[i]))
		#print(x1[i], y2[i])
plt.plot(x2,y2)
n = len(x2)
x_sq = [x*x for x in x2]
p = sum(x_sq)
q = sum(x2)
r = 0
for i in range(n):
	r += x2[i]*y2[i]
s = sum(y2)

print(p, q, r, s)
lam = (1/((n*p) - (q*q)))*((n*r)-(q*s))
c = (1/((n*p) - (q*q)))*((p*s)-(r*q))

print('Lambda = ', lam)
print('c = ', c)


line_x = np.linspace(0,4,1000)
line_y = []
for x in line_x:
	#y = (0.3163649927e0*x) + 0.3887284542e1
	#y = (8.72628079697) +(-2.60424676781*x)
	#y = (0.7824762174e1) +(-0.2345683086e1*x)
	y = (c) +(lam*x)
	line_y.append(y)
plt.plot(line_x,line_y)

"""
lam = 1705.081961
p = 0.000028
q = 0.005286
r = 0.047636
s = 9.012377
c = 344.174215 * (-(q*r) + (p*s))
print(c)
x2 = [i for i in range(1,601)]
y2 = [c*(2.7**(-lam*x)) for x in x2]
plt.plot(x2,y2)
"""
plt.title("Comparison of LSE fitting and original")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig('comparison.png')


"""
val = 'c'
Y = list(df[val])
plt.hist(Y, bins = 500)
plt.title("Histogram of " + val)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.ylim((0,50000))
plt.savefig(val +'.png')
plt.clf()
"""
