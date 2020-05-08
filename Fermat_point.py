import numpy as np
from math import sin, cos, pi, factorial, acos, atan
import pylab as pl
from matplotlib import collections as mc
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from shapely.geometry import LinearRing, Polygon
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
import random
import scipy.optimize as si
import scipy.optimize as so
from scipy.optimize import minimize

def dist(a, b):
    """Computes the distance between two points"""
    return (sum([(a[i] - b[i]) ** 2 for i in range(len(a))]) ** .5)

##draw saddle
#def fun(x, y):
#    return x**2 - y**2

nodes = []
for i in range(3):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    nodes.append((x,y))

print('nodes -> {}\nnodes[0] -> {}\nnodes[0][0] -> {}'.format(nodes,nodes[0],nodes[0][0]))
coord = [random.uniform(min([i[0] for i in nodes]), max([i[0] for i in nodes])),random.uniform(min([i[1] for i in nodes]), max([i[1] for i in nodes]))]
print(coord)

def cost(coord_,nodes):
    cost = 0
    cost = sum([dist(coord_,nodes[i]) for i in range(len(nodes))])
    return(cost)
print(cost(coord,nodes))

#get the optimize progress
#res_x = []
#ret = so.fmin(cost, coord, args = (nodes), callback=res_x.append)
#res_x = np.array(res_x).ravel()
#print(res_x)
#res_y = cost(res_x)
def fermat_point(coord,nodes,cost):
    xmin = min([i[0] for i in nodes])
    xmax = max([i[0] for i in nodes])
    ymin = min([i[1] for i in nodes])
    ymax = max([i[1] for i in nodes])
    bounds = ((xmin,xmax),(ymin,ymax))
    Iter = 10
    min_dist = [0,10]
    for i in range(Iter):
        ret = minimize(cost,coord,args=(nodes),method='Nelder-Mead',jac=None, bounds=bounds, tol=None, callback=None,options={'maxiter': 100})
        print('ret - > ',ret)
        if ret.fun<min_dist[1]:
            min_dist[0] = min_dist[1]
            min_dist[1] = ret.fun
            min_coord = []
            min_coord.append(ret.x)
    return(min_dist[1],min_coord)

fermat_distance = fermat_point(coord,nodes,cost)[0]
fermat_point = fermat_point(coord,nodes,cost)[1][0]
print('dist = ',fermat_distance)
print('opt coord = ',fermat_point)

nodes = Polygon(nodes)
x,y = nodes.exterior.xy
fig = plt.figure()

ax = fig.add_subplot(111) #projection='3d'
ax.plot(x, y, color='#6699cc', alpha=0.7,linewidth=3, solid_capstyle='round', zorder=2)
ax.plot(fermat_point[0],fermat_point[1],marker = 'o',color = '#DF0101')
for i in range(len(x)):
    ax.plot([x[i],fermat_point[0]], [y[i],fermat_point[1]], 'ro-',color = '#DF0101')
ax.set_xlabel('X')
ax.set_ylabel('Y')
#ax.set_zlabel('Z Label')
plt.show()

