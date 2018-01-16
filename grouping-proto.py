import pandas as pd

df = pd.read_csv("../data/redundantSamples_86_specter.csv")
par = 'id1'
nbh = 'id2'

grp_id = []
grp = []
count = 0

for index, row in df.iterrows():
    if index > 100:
        break
    count += 1
    print("Currently on row: ", count)
    flag = 0
    for j in range(len(grp_id)):
        if (row[par] in grp_id[j]) or (row[nbh] in grp_id[j]):
            if row[par] not in grp_id[j]:
                grp_id[j].append(row[par])
                grp[j].append([row[par], row['x1'], row['y1'], row['z1'],
                                row['f1'], row['n1']])

            if row[nbh] not in grp_id[j]:
                grp_id[j].append(row[nbh])
                grp[j].append([row[nbh], row['x2'], row['y2'], row['z2'],
                                row['f2'], row['n2']])

            flag = 1
    if flag == 0:
        new_grp_id = []
        new_grp_id.append(row[par])
        new_grp_id.append(row[nbh])
        grp_id.append(new_grp_id)

        new_grp = []
        new_grp.append([row[par], row['x1'], row['y1'], row['z1'],
                        row['f1'], row['n1']])
        new_grp.append([row[nbh], row['x2'], row['y2'], row['z2'],
                        row['f2'], row['n2']])
        grp.append(new_grp)

for i in range(len(grp_id)):
    print('Group by IDs', i+1, ' = ', grp_id[i])

for i in range(len(grp)):
    #print('Group ', i+1, ' = ', grp[i])
    print('\nGroup', i+1)
    print('Samples:')
    for j in range(len(grp[i])):
        print('Sample', j+1, ': ', grp[i][j])

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
