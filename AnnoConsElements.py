import numpy as np

f = open('./Results/ConservedRE_RE.txt')
a = f.readlines();f.close()
RE_SNP = []
for i in range(len(a)):
	a[i] = a[i].strip('\n').split('\t')
	RE_SNP.append(a[i][6])
f = open('./Results/CNCCNetwork_RE1_RE2.txt')
a = f.readlines();f.close()
RE12 = [[],[]]
for i in range(len(a)):
	a[i] = a[i].strip('\n').split('\t')
	RE12[0].append(a[i][0])
	RE12[1].append(a[i][1])
f = open('./Results/ConservedRE_Net_Sorted.txt')
a = f.readlines();f.close()
TG = [a[0].split('\t')[1]]
tmp = [];score = []
g = open('./Results/ConservedRE_Net_Filtered.txt','w')
for i in range(len(a)):
	a[i] = a[i].strip('\n').split('\t')
	if a[i][1] in TG and i < len(a)-1:
		b = a[i][0]+'\t'+a[i][1]+'\t'+a[i][2]+'\t'
		a[i][3] = a[i][3].split(';')
		for j in range(len(a[i][3])):
			if a[i][3][j] in RE_SNP:
				b += RE12[1][RE12[0].index(a[i][3][j])];
				b += ';'
		tmp.append(b.strip(';')+'\n');score.append(float(a[i][2]))
	else:
		mean_score = np.mean(score)
		for j in range(len(score)):
			if score[j] >= mean_score:
				g.write(tmp[j])
		TG.append(a[i][1])
		tmp = [];score = [float(a[i][2])]
		b = a[i][0]+'\t'+a[i][1]+'\t'+a[i][2]+'\t'
		a[i][3] = a[i][3].split(';')
		for j in range(len(a[i][3])):
			if a[i][3][j] in RE_SNP:
				b += RE12[1][RE12[0].index(a[i][3][j])];
				b += ';'
		tmp.append(b.strip(';')+'\n')
g.close()
