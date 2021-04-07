import sys
from collections import deque

def bfs(start):
        while start:
                dot=start.popleft()
                for j,l in direc1:
                        b,c=dot[1]+j, dot[2]+l
                        if b>=0 and c>=0 and b<n and c<m and mapp[b][c]=='0' and path[dot[0]][b][c]==0:
                                path[dot[0]][b][c]=path[dot[0]][dot[1]][dot[2]]+1
                                start.append([dot[0],b,c])
                for p,h in direc2: 
                        a,b,c=dot[0]+1, dot[1]+p, dot[2]+h
                        if a >=0 and b>=0 and c>=0 and a<k+1 and b<n and c<m and mapp[b][c]=='0' and path[a][b][c]==0:
                                path[a][b][c]=path[dot[0]][dot[1]][dot[2]]+1
                                start.append([a,b,c])
                                                                
direc1=((1,0),(-1,0),(0,1),(0,-1))
direc2=((1,2),(2,1),(-2,1),(-1,2),(-2,-1),(-1,-2),(2,-1),(1,-2))
k= int(sys.stdin.readline())
m, n = map(int, sys.stdin.readline().split())
mapp=[sys.stdin.readline().split() for i in range(n)] 
path=[[[0]*m for i in range(n)] for j in range(k+1)]
start=deque()
start.append([0,0,0])
bfs(start)
ans=m*n
while (k+1):
        if path[k][n-1][m-1]!=0:
                ans=min(ans,path[k][n-1][m-1])
        k-=1
if ans==m*n:
        print(-1)
else:
        print(ans)
