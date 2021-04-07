import sys
import copy

def check(arri,viru):
        v=copy.deepcopy(viru)
        arr=copy.deepcopy(arri)
        ans=0
        while v:
                tem=v.pop()
                ans+=1
                g=[[tem[0],tem[1]-1],[tem[0],tem[1]+1],[tem[0]-1,tem[1]],[tem[0]+1,tem[1]]]
                for y in g:
                        if (y[0]>=0) and (y[0]<h) and (y[1]>=0) and (y[1]<w):
                                if arr[y[0]][y[1]]==0:
                                        arr[y[0]][y[1]]=2
                                        v.append(y)

        return ans

h, w=map(int, sys.stdin.readline().split())
rom=[0]*h
cand=[]
viru=[]
for i in range(h):
        rom[i]=[]
        tem=sys.stdin.readline().split()
        for j in range(w):
                rom[i].append(int(tem[j]))
                if int(tem[j])==0:
                        cand.append([i,j])
                elif int(tem[j])==2:
                        viru.append([i,j])
s1=w*h-len(cand)-len(viru)+3
n=len(cand)
test=0
for p in range(n):
        a, b=cand[p][0], cand[p][1]
        for o in range(p+1,n):
                c,d=cand[o][0],cand[o][1]
                for r in range(o+1,n):
                        room=copy.deepcopy(rom)
                        s,t=cand[r][0],cand[r][1]
                        room[a][b],room[c][d],room[s][t]=1,1,1
                        test=max(test,(w*h-check(room,viru)-s1))
                        
print(test)
