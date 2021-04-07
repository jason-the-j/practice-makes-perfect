import sys
from collections import deque

def bfs(st,zero):
        while st:
                dot=st.popleft()
                for i,j,k in direction:
                        a,b,c=dot[0]+i, dot[1]+j, dot[2]+k
                        if a >=0 and b>=0 and c>=0 and a<h and b<n and c<m:
                                if box[a][b][c]==0:
                                        st.append([a,b,c])
                                        box[a][b][c]=box[dot[0]][dot[1]][dot[2]]+1
                                        zero-=1
        return dot, zero

direction=((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))
m,n,h=map(int, sys.stdin.readline().split())
box=[[[0]*m for i in range(n)] for j in range(h)]
start, zero= deque(),0
for i in range(h):
        for j in range(n):
                tem=sys.stdin.readline().split()
                for k in range(m):
                        box[i][j][k]=int(tem[k])
                        if int(tem[k])==1:
                                start.append([i,j,k])
                        elif int(tem[k])==0:
                                zero+=1
if zero==0:
        print(0)
else:
        spot,zero=bfs(start,zero)
        if not zero:
                print(box[spot[0]][spot[1]][spot[2]]-1)
        else:
                print(-1)
