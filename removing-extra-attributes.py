import pandas as pd
import json
import os

PATH = '../json_data_dump/'
O_PATH = '../json_data_dump_2/'
grp_id = 'grp0'

print('finding file names')
file_names = os.listdir(PATH)

print(len(file_names))
print(file_names[56037])
"""
for name in file_names:
    print(name)
print(len(file_names))
"""

cnt = 0
for name in file_names:
    cnt += 1
    data_path = PATH + name
    print("Finding for " + name)
    with open(data_path) as infile:
        final_dump = {}
        data = json.load(infile)
        final_dump['lvl1_grp_id'] = data['lvl1_grp_id']
        final_dump['nodes'] = data['nodes']

        revised_edges = []
        for i in range(len(data['edges'])):
            revised_edges.append({
                    'node1': data['edges'][i]['node1'],
                    'node2': data['edges'][i]['node2'],
                })
        #print('PRINTING')
        #print(data['lvl1_grp_id'][3:])
        #print(int(data['lvl1_grp_id'][3:]))

        final_dump['edges'] = revised_edges
        with open(O_PATH + data['lvl1_grp_id'] + ".json" , 'w') as outfile:
                json.dump(final_dump, outfile)
