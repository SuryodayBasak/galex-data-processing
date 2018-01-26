import pandas as pd
import json

df = pd.read_csv("../data/distanceMatches_specter.csv",
                    dtype={'obsid1': object, 'obsid2': object,
                            'peid1': object, 'peid2': object})

grp_id = []
grp_edges = []
grp = []
count = 0

for index, row in df.iterrows():
    #if index > 10000:
    #    break
    count += 1
    print("Currently on row: ", count, "/ 154924")
    flag = 0
    for j in range(len(grp_id)):
        if (row['obsid1'] in grp_id[j]) or (row['obsid2'] in grp_id[j]):
            grp_edges[j].append({"node1" : row['obsid1'],
                                "node2" : row['obsid2'],
                                "dist_mag" : row['mag_dist'],
                                "dist_flux" : row['flux_dist'],
                                "dist_int" : row['int_dist']})
            if row['obsid1'] not in grp_id[j]:
                grp_id[j].append(row['obsid1'])
                #grp[j].append([row[par], row['x1'], row['y1'], row['z1'],
                #                row['f1'], row['n1']])
                grp[j].append({"obsid" : row['obsid1'], "peid" : row['peid1'],
                                "ra" : row['ra1'], "dec" : row['dec1'],
                                "glat" : row['glat1'], "glon" : row['glon1'],
                                "x" : row['x1'], "y" : row['y1'],
                                "z" : row['z1'], "fuv_mag" : row['fuv_mag1'],
                                "nuv_mag" : row['nuv_mag1'],
                                "fuv_flux" : row['fuv_flux1'],
                                "nuv_flux" : row['nuv_flux1'],
                                "fuv_int" : row['fuv_int1'],
                                "nuv_int" : row['nuv_int1']})

            if row['obsid2'] not in grp_id[j]:
                grp_id[j].append(row['obsid2'])
                grp[j].append({"obsid" : row['obsid2'], "peid" : row['peid2'],
                                "ra" : row['ra2'], "dec" : row['dec2'],
                                "glat" : row['glat2'], "glon" : row['glon2'],
                                "x" : row['x2'], "y" : row['y2'],
                                "z" : row['z2'], "fuv_mag" : row['fuv_mag2'],
                                "nuv_mag" : row['nuv_mag2'],
                                "fuv_flux" : row['fuv_flux2'],
                                "nuv_flux" : row['nuv_flux2'],
                                "fuv_int" : row['fuv_int2'],
                                "nuv_int" : row['nuv_int2']})
            flag = 1
            break

    if flag == 0:
        new_grp_id = []
        new_grp_id.append(row['obsid1'])
        new_grp_id.append(row['obsid2'])
        grp_id.append(new_grp_id)

        new_grp_edges = []
        new_grp_edges.append({"node1" : row['obsid1'],
                            "node2" : row['obsid2'],
                            "dist_mag" : row['mag_dist'],
                            "dist_flux" : row['flux_dist'],
                            "dist_int" : row['int_dist']})
        grp_edges.append(new_grp_edges)

        new_grp = []
        new_grp.append({"obsid" : row['obsid1'], "peid" : row['peid1'],
                        "ra" : row['ra1'], "dec" : row['dec1'],
                        "glat" : row['glat1'], "glon" : row['glon1'],
                        "x" : row['x1'], "y" : row['y1'],
                        "z" : row['z1'], "fuv_mag" : row['fuv_mag1'],
                        "nuv_mag" : row['nuv_mag1'],
                        "fuv_flux" : row['fuv_flux1'],
                        "nuv_flux" : row['nuv_flux1'],
                        "fuv_int" : row['fuv_int1'],
                        "nuv_int" : row['nuv_int1']})

        new_grp.append({"obsid" : row['obsid2'], "peid" : row['peid2'],
                        "ra" : row['ra2'], "dec" : row['dec2'],
                        "glat" : row['glat2'], "glon" : row['glon2'],
                        "x" : row['x2'], "y" : row['y2'],
                        "z" : row['z2'], "fuv_mag" : row['fuv_mag2'],
                        "nuv_mag" : row['nuv_mag2'],
                        "fuv_flux" : row['fuv_flux2'],
                        "nuv_flux" : row['nuv_flux2'],
                        "fuv_int" : row['fuv_int2'],
                        "nuv_int" : row['nuv_int2']})

        grp.append(new_grp)

for i in range(len(grp_id)):
    print('Group by IDs', i+1, ' = ', grp_id[i])

for i in range(len(grp)):
    grp_json = {}
    grp_json["lvl1_grp_id"] = "grp"+str(i + 1)
    grp_json["nodes"] = grp[i]
    grp_json["edges"] = grp_edges[i]

    with open("../json_data_dump/grp"+str(i)+".json" , 'w') as outfile:
        json.dump(grp_json, outfile)
    #n = len(grp_json["obs"])
    #grp_json["e_fuv"] = sum(smpl["fuv"] for smpl in grp_json["obs"])/n
    #grp_json["e_nuv"] = sum(smpl["nuv"] for smpl in grp_json["obs"])/n
    #grp_json["e_x"] = sum(smpl["x"] for smpl in grp_json["obs"])/n
    #grp_json["e_y"] = sum(smpl["y"] for smpl in grp_json["obs"])/n
    #grp_json["e_z"] = sum(smpl["z"] for smpl in grp_json["obs"])/n
    #grp_json["e_fn"] = sum(smpl["diff_fn"] for smpl in grp_json["obs"])/n

    print(grp_json)
    print('\n')
    """
    print('Group ', i+1, ' = ', grp[i])
    print('\nGroup', i+1)
    print('Samples:')
    for j in range(len(grp[i])):
        print('Sample', j+1, ': ', grp[i][j])
    """

"""
for i in range(len(data)):
    flag = 0
    for j in range(len(grp)):
        if (data[i][par] in grp[j]) or (data[i][nbh] in grp[j]):
            if data[i][par] not in grp[j]:
                grp[j].append(data[i][par])
            if data[i][nbh] not in grp[j]:
                grp[j].append(data[i][nbh])
            flag = 1
    if flag == 0:
        new_grp = []
        new_grp.append(data[i][par])
        new_grp.append(data[i][nbh])
        grp.append(new_grp)

for i in range(len(grp)):
    print('Group ', i+1, ' = ', grp[i])
"""
