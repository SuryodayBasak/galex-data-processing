import json
import os
import numpy as np

PATH = '../json_data_dump_2/'
grp_id = 'grp0'
print('finding file names')
file_names = os.listdir(PATH)

cnt_histogram = {
            2:0,
            3:0,
            4:0,
            5:0,
            6:0
        }

ranking = []
cnt = 0
for name in file_names:
    node_ids = []   #List to contain only node IDs
    cnt += 1
    data_path = PATH + name
    print("Currently on " + str(cnt) + "th file")

    with open(data_path) as infile:
        final_dump = {}
        data = json.load(infile)

        for node in data['nodes']:  #Forming complete list of IDs
            node_ids.append(node['obsid'])

    infile.close()

    """
    Sorting the IDs in increasing order so that adjacency matrices make
    sense
    """
    node_ids.sort()
    n = len(node_ids)   #Size of adjacency matrices
    adj_mat = np.zeros((n, n), np.bool_) #initializing adjacency matrix

    for i in range(0, n):
        row_obj_id = node_ids[i]

        for j in range(0, n):
            col_obj_id = node_ids[j]

            if row_obj_id == col_obj_id:
                adj_mat[i, j] = 1

            else:
                for edge in data['edges']:
                    if (edge['node1'] == row_obj_id and
                        edge['node2'] == col_obj_id):
                        adj_mat[i, j] = 1


    #print(adj_mat)
    #if 0 in adj_mat:
