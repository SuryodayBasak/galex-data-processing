import pandas as pd
import csv
import json
import os

PATH = '../json_data_dump_2/'
O_PATH = '../scrutiny-thresh-1.0-2-samples/'
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
    cnt += 1
    data_path = PATH + name
    print("Currently on " + str(cnt) + "th file")
    with open(data_path) as infile:
        final_dump = {}
        data = json.load(infile)
        n_nodes = len(data['nodes'])
        cnt_histogram[n_nodes] += 1

        if len(data['nodes']) == 2:

            d_fuv = abs(data['nodes'][0]['fuv_mag']-data['nodes'][1]['fuv_mag'])
            d_nuv = abs(data['nodes'][0]['nuv_mag']-data['nodes'][1]['nuv_mag'])
            if (d_fuv > 1.0 or d_nuv > 1.0):
                outlier_rec = [['ID', 'RA', 'DEC'],
                                [data['nodes'][0]['obsid'],
                                data['nodes'][0]['ra'],
                                data['nodes'][0]['dec']],
                                [data['nodes'][1]['obsid'],
                                data['nodes'][1]['ra'],
                                data['nodes'][1]['dec']]]

                with open(O_PATH + data['lvl1_grp_id'] +'.csv', "w") as f:
                    writer = csv.writer(f)
                    writer.writerows(outlier_rec)

                if d_fuv > d_nuv:
                    attr = d_fuv
                else:
                    attr = d_nuv

                ranking.append([attr, data['lvl1_grp_id']])

print(cnt_histogram)
ranking.sort()

with open(O_PATH + 'ranking.csv', "w") as f:
    writer = csv.writer(f)
    writer.writerows(ranking)
