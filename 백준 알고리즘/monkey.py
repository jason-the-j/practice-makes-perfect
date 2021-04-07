import sys
from collections import deque

def bfs(start):
        while start:
                dot=start.popleft()
                for _,j,l in direc1:
                        b,c=dot[1]+j, dot[2]+l
                        if b>=0 and c>=0 and b<n and c<m and mapp[b][c]=='0' and path[dot[0]][b][c]==0:
                                path[dot[0]][b][c]=path[dot[0]][dot[1]][dot[2]]+1
                                start.append([dot[0],b,c])
                for i,j,l in direc2:
                        a,b,c=dot[0]+i, dot[1]+j, dot[2]+l
                        if a >=0 and b>=0 and c>=0 and a<k+1 and b<n and c<m and mapp[b][c]=='0' and path[a][b][c]==0:
                                path[a][b][c]=path[dot[0]][dot[1]][dot[2]]+1
                                start.append([a,b,c])
                                                                
direc1=((0,1,0),(0,-1,0),(0,0,1),(0,0,-1))#4
direc2=((1,2,1),(1,1,2),(1,-2,1),(1,-1,2),(1,-2,-1),(1,-1,-2),(1,2,-1),(1,1,-2))#8
k= int(sys.stdin.readline())
m, n = map(int, sys.stdin.readline().split())
mapp=[sys.stdin.readline().split() for i in range(n)] #nm
path=[[[0]*m for i in range(n)] for j in range(k+1)]
start=deque()
start.append([0,0,0])
bfs(start)
mem=k
while (k+1):
        if path[k][n-1][m-1]!=0:
                print(path[k][n-1][m-1])
                break
        k-=1
else:
        while (mem-1):
                if path[mem][n-2][m-3]!=0:
                        print(path[mem][n-2][m-3]+1)
                        break
                elif path[mem][n-3][m-2]!=0:
                        print(path[mem][n-3][m-2]+1)
                        break
                mem-=1
        else:
                if n==1 and m==1:
                        print(0)
                else:
                        print(-1)
