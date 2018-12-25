import numpy as np
import math

def get_distance(data1, data2):
    points = zip(data1, data2)
    diffs_squared_distance = [pow(float(a) - float(b), 2) for (a, b) in points]
    return math.sqrt(sum(diffs_squared_distance))

def k_min(lst,k):
    a=sorted(lst)[1:k+1]
    return a

infile = open("heart_trainSet.txt")
trn = infile.read().splitlines()
infile.close()
for i in range (len(trn)):
    trn[i] = trn[i].split(',')
    for j in range (len(trn[i])):
        trn[i][j]= float(trn[i][j])
trn_arr = np.array(trn)

infile = open("heart_trainLabels.txt")
lab = infile.readlines()
infile.close()
for i in range (len(lab)):
    lab[i] = int(lab[i].strip())
lab_arr = np.array(lab)
lab_arr= np.reshape(lab_arr,(len(lab_arr),1))

dist=[0]*len(trn)
err=[0]*10
for k in range(1,11):
    for i in range (len(trn)):
        for j in range (len(trn)):
            if i==j:
                dist[i]=0.
            else:
                dist[j]=(get_distance(trn_arr[i],trn_arr[j]))
        k_min_dist=k_min(dist,k)
        vote_list=[]
        for n in k_min_dist:
            vote_list.append(lab_arr[dist.index(n)]) 
        vote = int(sum(vote_list))
        if vote*lab_arr[i] <0:
            err[k-1] =err[k-1]+ 1
print "Total Error: ",err
k_opt = min(err)
for i in range (len(err)):
    err[i]=err[i]/float(len(trn))
print "Normalized Error: ",err


infile = open("heart_testSet.txt")
tst = infile.read().splitlines()
infile.close()
for i in range (len(tst)):
    tst[i] = tst[i].split(',')
    for j in range (len(tst[i])):
        tst[i][j]= float(tst[i][j])
tst_arr = np.array(tst)

tst_lab=[]
for i in range (len(tst)):
    for j in range (len(trn)):
        dist[j]=(get_distance(tst_arr[i],trn_arr[j]))
    k_min_dist=k_min(dist,k_opt)
    vote_list=[]
    for n in k_min_dist:
        vote_list.append(lab_arr[dist.index(n)]) 
    vote = int(sum(vote_list))
    if vote <0:
        tst_lab.append(-1)
    elif vote==0:
        tst_lab.append(0)
    elif vote>0:
        tst_lab.append(1)
print tst_lab