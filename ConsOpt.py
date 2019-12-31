import numpy as np
import re

###set parametert
alpha = 37*100;beta = 1/20;theta = 200;K = 6;gamma = 0.1*2*K*alpha

def GetRes(meanS, meanC, L, thre, cut, chros, start):
	Cij = np.zeros(L)
	Sij_new = meanS - theta;Sij_old = -1
	while np.abs(Sij_new-Sij_old) > thre:
		Sij_old = Sij_new
		Cij_up = np.append(np.append(0,Cij[0:L-2]),0)
		Cij_down = np.append(np.append(0,Cij[2:L]),0)
		Cij = meanC + beta/(2*K*alpha)*Sij_new + gamma/(2*K*alpha) * (Cij_up+Cij_down)
		Cij = (Cij-np.min(Cij))/np.max(Cij)
		Sij_new = meanS + beta/(2*K)*np.sum(Cij) - theta
	C01 = ''.join(((Cij > cut).astype('int')).astype('str'))
	st = [sti.span()[0]+start for sti in re.finditer('01', C01)]
	ed = [sti.span()[0]+start-1 for sti in re.finditer('10', C01)]
	RE = [chros+'_'+str(st[i])+'_'+str(ed[i]) for i in range(len(st))]
	return Sij_new, RE

Net = []
for i in range(K):
	f = open('./Input/CNCCNetwork_'+str(i+1)+'.txt')
	a = f.readlines();f.close()
	Net.append([])
	for j in range(len(a)):
		a[j] = a[j].strip('\n').split('\t')
		a[j][4] = a[j][4].split(';')
		Net[i].append([a[j][0],a[j][1],float(a[j][2]),a[j][4]])
g = open('./Results/CNCCNetwork.txt','w')
for i in range(len(a)):
	Sijk = [];CRM = [];st = [];ed = [];chrom = ''
	for j in range(K):
		Sijk.append(Net[j][i][2])
		CRM.append(Net[j][i][3])
		if Net[j][i][3][0] != '' and Net[j][i][3][0] != '*':
			for k in range(len(Net[j][i][3])):
				Net[j][i][3][k] = Net[j][i][3][k].split('_')
				chrom = Net[j][i][3][k][0]
				st.append(int(Net[j][i][3][k][1]))
				ed.append(int(Net[j][i][3][k][2]))
	if len(st) > 0:
		st = np.min(st);ed = np.max(ed)
		L = ed - st + 3
		Cijk = np.zeros((K,L))
		for j in range(K):
			if CRM[j][0] != '' and CRM[j][0] != '*':
				for k in range(len(CRM[j])):
					Cijk[j][int(CRM[j][k][1])-st+1:int(CRM[j][k][2])+2-st] = 1
		meanCijk = np.sum(Cijk,0)/K;meanSijk = np.mean(Sijk)
		Sij, RE = GetRes(meanSijk,meanCijk,L,0.1,0.3,chrom,st)
		if len(RE) > 0 and Sij > 0:
			FC = ''
			for l in range(len(RE)):
				FC += RE[l]+';'
			g.write(Net[0][i][0]+'\t'+Net[0][i][1]+'\t'+str(Sij)+'\t'+FC.strip(';')+'\n')
g.close()
