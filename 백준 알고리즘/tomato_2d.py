import sys
from collections import deque

def bfs(st,zero):
        while st:
                dot=st.popleft()
                for i,j in direction:
                        a,b=dot[0]+i, dot[1]+j
                        if a >=0 and b>=0 and a<n and b<m:
                                if box[a][b]==0:
                                        st.append([a,b])
                                        box[a][b]=box[dot[0]][dot[1]]+1
                                        zero-=1
        return dot, zero

direction=((-1, 0), (1, 0), (0, -1), (0, 1))
m,n=map(int, sys.stdin.readline().split())
box=[[0]*m for i in range(n)]
start, zero= deque(),0
for j in range(n):
        tem=sys.stdin.readline().split()
        for k in range(m):
                box[j][k]=int(tem[k])
                if int(tem[k])==1:
                        start.append([j,k])
                elif int(tem[k])==0:
                        zero+=1
if zero==0:
        print(0)
else:
        spot,zero=bfs(start,zero)
        if not zero:
                print(box[spot[0]][spot[1]]-1)
        else:
                print(-1)
