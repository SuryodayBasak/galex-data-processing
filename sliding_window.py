import pandas as pd
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')

"""
random changes
def cosine_similarity(saddle, cat_entity):
	saddle_x = float(saddle['X'])
	saddle_y = float(saddle['Y'])
	saddle_z = float(saddle['Z'])
	
	cat_x = float(cat_entity['X'])
	cat_y = float(cat_entity['Y'])
	cat_z = float(cat_entity['Z'])
	
	return ((saddle_x*cat_x) + (saddle_y*cat_y) +
	(saddle_z*cat_z))/(math.sqrt(saddle_x**2 + saddle_y**2 + saddle_z**2)
	+ math.sqrt(cat_x**2 + cat_x**2 + cat_x**2))
"""	


def cosine_similarity(saddle, cat_entity):
	saddle_x = float(saddle['X'])
	saddle_y = float(saddle['Y'])
	saddle_z = float(saddle['Z'])
	
	cat_x = float(cat_entity['X'])
	cat_y = float(cat_entity['Y'])
	cat_z = float(cat_entity['Z'])
	
	cos_sim = ((saddle_x*cat_x) + (saddle_y*cat_y) +
	(saddle_z*cat_z))/(math.sqrt(saddle_x**2 + saddle_y**2 + saddle_z**2)
	+ math.sqrt(cat_x**2 + cat_x**2 + cat_x**2))
	
	if cos_sim <= math.cos(math.radians(0.0013889)):
		cos_sim = 0
	
	return cos_sim
	
	
#Reading data
DATA_PATH = 'testing_phase_1_specter.csv'
data = pd.read_csv(DATA_PATH, usecols=['objid','X','Y','Z'])
#random_saddle = data.sample(n=1)

X_BOUND = 1.0
Y_BOUND = 1.0
Z_BOUND = 1.0

"""
temp_df = data[(data['X'] < float(random_saddle['X']) + X_BOUND) 
		& (data['X'] > float(random_saddle['X']) - X_BOUND)
		& (data['Y'] < float(random_saddle['Y']) + Y_BOUND) 
		& (data['Y'] > float(random_saddle['Y']) - Y_BOUND)
		& (data['Z'] < float(random_saddle['Z']) + Z_BOUND) 
		& (data['Z'] > float(random_saddle['Z']) - Z_BOUND)]
print(temp_df)
"""

iteration = 0
similarity_list = []

#book-keeping:
outer_count = 0

#for index, saddle in temp_df.iterrows():
for index_, saddle in data.iterrows():
	outer_count += 1
	inner_count = 0
	#for index, row in temp_df.iterrows():
	for index, row in data.iterrows():
		cos_similarity = cosine_similarity(saddle, row)
		if cos_similarity != 0:
			similarity_list.append(cos_similarity)
		inner_count += 1
		print(outer_count, inner_count)
	#print(iteration)

print(similarity_list)
print('Number of cross-similarities:', len(similarity_list))	
#similarity_list = similarity_list.sort()
"""
for val in similarity_list:
	print(val)
"""
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
