import sys
from collections import deque

def dfs(o):
        visitd[o]=1
        print(str(o),end=' ')
        for i in route[o]:
                if visitd[i]==0:
                        dfs(i)
def bfs(o):
        cri=deque()
        cri.append(o)
        while cri:
                piv=cri.popleft()
                if visitb[piv]==0:
                        print(str(piv),end=' ')
                        visitb[piv]=1
                        for i in route[piv]:
                                        cri.append(i)

v, m, start=map(int, sys.stdin.readline().split())
route=[[] for q in range(v+1)]
for k in range(m):
        a,b=map(int, sys.stdin.readline().split())
        route[a].append(b)
        route[b].append(a)
for u in range(v+1):
        route[u].sort()
        
visitd, visitb=[0]*(v+1),[0]*(v+1)
dfs(start)
print()
bfs(start)

