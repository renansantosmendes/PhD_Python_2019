import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

pareto = pd.read_csv('pareto3fo.csv', sep=',',header=None)
pareto.columns = 'F1 F2 F3'.split()

pop = pd.read_csv('pop_inicial_3fo.csv', sep=',',header=None)
pop.columns = 'F1 F2 F3'.split()

fig = plt.figure()
ax = Axes3D(fig)

X = pareto['F1'].values
Y = pareto['F2'].values
Z = pareto['F3'].values

ax.scatter(X,Y,Z, label = 'Pareto')

X = pop['F1'].values
Y = pop['F2'].values
Z = pop['F3'].values

ax.scatter(X,Y,Z, label = 'População Inicial')
plt.legend()
plt.show()