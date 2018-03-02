import json
import os
import numpy as np
import pandas as pd
import csv

PATH = '../json_data_dump_2/'
BAD_GRP_PATH = '../grps-bad/json/'
GOOD_GRP_PATH = '../grps-good/json/'
COL_NAMES = ['grpId', 'cx', 'cy', 'cz', 'ra', 'dec']
CENT_PATH = '../grps-good/centroids/'
good_names = os.listdir(PATH)
bad_names = os.listdir(BAD_GRP_PATH)

for grp in bad_names:
    good_names.remove(grp)

centroids = [['grpId', 'x', 'y', 'z', 'r', 'dec']]

n = len(good_names)
cnt = 0

for grp in good_names:
    cnt += 1

    data_path = PATH + grp
    x_all = []
    y_all = []
    z_all = []
    ra_all = []
    dec_all = []

    with open(data_path) as infile:
        final_dump = {}
        data = json.load(infile)

        for node in data['nodes']:
            #print(data['lvl1_grp_id'])
            #print(node)
            #print('')
            x_all.append(node['x'])
            y_all.append(node['y'])
            z_all.append(node['z'])
            ra_all.append(node['ra'])
            dec_all.append(node['dec'])

    infile.close()

    cx = sum(x_all)/len(x_all)
    cy = sum(y_all)/len(y_all)
    cz = sum(z_all)/len(z_all)
    ra = sum(ra_all)/len(ra_all)
    dec = sum(dec_all)/len(dec_all)

    obj_centroid_data = [data['lvl1_grp_id'], cx, cy, cz, ra, dec]
    centroids.append(obj_centroid_data)
    #print(obj_centroid_data)
    print(str(cnt) + '/' + str(n))

with open(CENT_PATH + 'centroids.csv', "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for row in centroids:
            writer.writerow(row)
csv_file.close()
