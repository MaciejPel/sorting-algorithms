from timeit import default_timer as timer
from copy import deepcopy
from sorts import insertionSort, selectionSort, heapSort, mergeSort, quickSortIterative
import random
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
import sys
sys.setrecursionlimit(10000000)

methods=[insertionSort, selectionSort, heapSort, mergeSort]

def randomSubset(size=10000,max=100000000):
    return random.sample(range(max),size)

def compare_algorithm(fun, *args):
    start=timer()
    fun(*args)
    endtime=timer()-start
    result.append([fun.__name__+'()', endtime])
    return result

result=[]
for j in range(1, 25002, 25000):
    tc = randomSubset(j)
    for i in methods:
        compare_algorithm(i,deepcopy(tc))
        result[-1].append(j)

x,x1,x2,x3,x4,x5,x6=[],[],[],[],[],[],[]
y,y1,y2,y3,y4,y5,y6=[],[],[],[],[],[],[]
czas=0
for j in result:
    if j[0]=='insertionSort()':
        x.append([j[2]])
        y.append([j[1]])
    elif j[0]=='selectionSort()':
        x1.append([j[2]])
        y1.append([j[1]])
    elif j[0]=='mergeSort()':
        x2.append([j[2]])
        y2.append([j[1]])
    elif j[0]=='heapSort()':
        x3.append([j[2]])
        y3.append([j[1]])
    elif j[0]=='quickSort()':
        x4.append([j[2]])
        y4.append([j[1]])
    czas+=j[1]

# x=np.array(x).squeeze()
# y=np.array(y).squeeze()
# x1=np.array(x1).squeeze()
# y1=np.array(y1).squeeze()
# x2=np.array(x2).squeeze()
# y2=np.array(y2).squeeze()
# x3=np.array(x3).squeeze()
# y3=np.array(y3).squeeze()
# x4=np.array(x4).squeeze()
# y4=np.array(y4).squeeze()
# x5=np.array(x5).squeeze()
# y5=np.array(y5).squeeze()
# x6=np.array(x6).squeeze()
# y6=np.array(y6).squeeze()
# xn = np.linspace(x.min(), x.max(),500)
# f = interp1d(x, y, kind='quadratic')
# ys=f(xn)
# x1n = np.linspace(x1.min(), x1.max(),500)
# f1 = interp1d(x1, y1, kind='quadratic')
# y1s=f1(x1n)
# x2n = np.linspace(x2.min(), x2.max(),500)
# f2 = interp1d(x2, y2, kind='quadratic')
# y2s=f2(x2n)
# x3n = np.linspace(x3.min(), x3.max(),500)
# f3 = interp1d(x3, y3, kind='quadratic')
# y3s=f3(x3n)
# x4n = np.linspace(x4.min(), x4.max(),500)
# f4 = interp1d(x4, y4, kind='quadratic')
# y4s=f4(x4n)
# x5n = np.linspace(x5.min(), x5.max(),500)
# f5 = interp1d(x5, y5, kind='quadratic')
# y5s=f5(x5n)
# x6n = np.linspace(x6.min(), x6.max(),500)
# f6 = interp1d(x6, y6, kind='quadratic')
# y6s=f6(x6n)

# plt.plot(x, y, label = "quickSort")
plt.plot(x, y, label = "insertionSort")
plt.plot(x1, y1, label = "selectionSort")
plt.plot(x2, y2, label = "mergeSort")
plt.plot(x3, y3, label = "heapSort")
plt.plot(x4, y4, label = "quickSort")

plt.title(str(round(czas/60,2))+'min dla max '+str(result[-1][2])+ ' co '+ str(result[-1][2]-result[-8][2]))
plt.legend()
plt.show()