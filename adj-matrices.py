import json
import os
import numpy as np
import pandas as pd
import csv

PATH = '../json_data_dump_2/'
ADJ_MAT_PATH = '../bad-grps/adj-mat/'
SPLIT_GRP_PATH = '../bad-grps/json/'
GVIEW_TABLES_PATH = '../bad-grps/gview-tables/'
print('finding file names')
file_names = os.listdir(PATH)

cnt = 0
n_probs = 0

for name in file_names:
    node_ids = []   #List to contain only node IDs
    cnt += 1
    data_path = PATH + name
    #print("Currently on " + str(cnt) + "th file")

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
    adj_mat = np.zeros((n, n), np.int8) #initializing adjacency matrix

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
                        adj_mat[j, i] = 1 #be careful about this...
                        """
                        Since the adjacency matrix needs to be symmetric,
                        the elements at position (i,j) and (j,i) must both
                        be the same. And if one of them is equal to 1, even the
                        other must be equal to 1.
                        """


    """
    If there are entries in the adjacency with no edges between some nodes, we
    need to take a look at them and use a method to handle such cases.
    """

    if 0 in adj_mat:
        n_probs = n_probs + 1
        print('Number of groups with issues: ' + str(n_probs)
            + ' || ' + name)

        adj_mat_fname = ADJ_MAT_PATH + name[:-5] + '.csv'
        grp_fname = SPLIT_GRP_PATH + name[:-5] + '.csv'
        gview_table_fname = GVIEW_TABLES_PATH + name[:-5] + '.csv'

        #Writing out the adjacency matrix
        adj_mat_df = pd.DataFrame(adj_mat, index=node_ids, columns=node_ids)
        adj_mat_df.to_csv(adj_mat_fname, index=True, header=True, sep=',')

        #Writing out the json files of the outliers
        with open(grp_fname , 'w') as outfile:
            json.dump(data, outfile)
        outfile.close()

        #Writing out the CSV files with objid, ra, dec of the all the outliers
        gview_table = [['ID', 'RA', 'DEC']]
        for node in data['nodes']:
            gview_table.append([node['obsid'], node['ra'], node['dec']])

        with open(gview_table_fname , "w") as outfile:
            writer = csv.writer(outfile)
            writer.writerows(gview_table)
        outfile.close()

        #print(adj_mat)
        #np.savetxt(name[:-5]+'.csv', adj_mat, delimiter="\t")
        #print(data)
