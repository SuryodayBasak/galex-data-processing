import pandas as pd
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Reading data
DATA_PATH = 'testing_phase_1_specter.csv'
data = pd.read_csv(DATA_PATH, usecols=['objid','X','Y','Z'])
random_saddle = data.sample(n=1)

X_BOUND = 1.0
Y_BOUND = 1.0
Z_BOUND = 1.0

temp_df = data[(data['X'] < float(random_saddle['X']) + X_BOUND) 
		& (data['X'] > float(random_saddle['X']) - X_BOUND)
		& (data['Y'] < float(random_saddle['Y']) + Y_BOUND) 
		& (data['Y'] > float(random_saddle['Y']) - Y_BOUND)
		& (data['Z'] < float(random_saddle['Z']) + Z_BOUND) 
		& (data['Z'] > float(random_saddle['Z']) - Z_BOUND)]
		
print(temp_df)

#print(random_saddle['X']+1)
#k = random_saddle['X']+1.0
#print(k)
#print(float(k))
#print(type(1.0))
#print(type(k))
#temp_df = data[data['X'] < k]
#print(temp_df)
"""
x_bounds = math.cos(math.radians(0.0013889))*math.cos(math.radians(0.0013889))
y_bounds = math.cos(math.radians(0.0013889))*math.cos(math.radians(0.0013889))
z_bounds = math.cos(math.radians(0.0013889))
print(x_bounds, y_bounds, z_bounds)
"""

"""
print(math.cos(0))
print(math.cos(math.radians(90)))
0.0013889
x = cos(0.0013889)*cos(0.0013889)
y = sin(0.0013889)*cos(0.0013889)
z = sin(0.0013889)
"""
