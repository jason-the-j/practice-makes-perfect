import sys
import math
                
def dfs(iceb):
        glc=[glc_base[j][:] for j in range(n)]
        stack=[iceb[0]]
        iceb=[]
        while stack:
                count=0
                dot=stack.pop() #dot=[x,y]
                for i in range(4):
                        a, b=dot[0]+s[i], dot[1]+k[i]
                        if glc_base[a][b]>0 and visited[a][b]==0:
                                stack.append([a,b])
                                visited[a][b]=1

                        if glc_base[a][b]==0:
                                count+=1

                glc[dot[0]][dot[1]]=glc_base[dot[0]][dot[1]]-count
                if glc[dot[0]][dot[1]]<=0:
                        glc[dot[0]][dot[1]]=0
                        counter[dot[0]][dot[1]]=math.inf
                else:
                        counter[dot[0]][dot[1]]+=1
                        iceb.append(dot)
        return glc, iceb                                                                                                                                                                                                                                                                          

s=[1,-1,0,0]
k=[0,0,1,-1]
n, m = map(int, sys.stdin.readline().split())
iceb=[]
counter=[[math.inf]*m for _ in range(n)]
glc_base=[[] for _ in range(n)]
for _ in range(n):
        tem=sys.stdin.readline().split()
        for q in range(m):
                glc_base[_].append(int(tem[q]))
                if int(tem[q])!=0:
                        iceb.append([_,q])
                        counter[_][q]=0
                        
yr=0
while iceb:
        check=[0]*n
        visited=[[0]*m for _ in range(n)]
        glc_base, iceb=dfs(iceb)
        yr+=1
        for i in range(n):
                check[i]=min(counter[i])
        if min(check)!=yr:
                if min(check)==math.inf:
                        yr=0
                        break
                else:
                        yr-=1
                        break
                
print(yr)
