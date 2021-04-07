import math
from collections import deque
def check(a,b,c):
        if math.isinf(spl[a]) and math.isfinite(spl[b]):
                spl[a]=spl[b]-c
                return a
        elif math.isfinite(spl[a]) and math.isinf(spl[b]):
                spl[b]=spl[a]+c
                return b
        else:
                if math.isinf(spl[a]*spl[b]):
                        save[a].append([b,c])
                        save[b].append([a,-c])
                return 0
for j in range(int(input())):
        n,m=map(int, input().split())
        spl=[math.inf]*(n+1)
        save=[[] for ho in range(n+1)]
        res=[]
        count=0
        for _ in range(m):
                a=input().split()
                if len(a)>3:
                        x,y,z=int(a[1]),int(a[2]),int(a[3])
                        if not count:
                                spl[x]=0
                                spl[y]=z
                                count=1
                        else:
                                nex=deque()
                                nex.append(check(x,y,z))
                                while nex:
                                        temp=nex.popleft()
                                        for r in save[temp]:
                                                spl[r[0]]=spl[temp]+r[1]
                                                nex.append(r[0])                                             
                                        save[temp]=[]
                        
                else:
                        x,y=int(a[1]),int(a[2])                              
                        if math.isinf(spl[x]*spl[y]) or math.isnan(spl[x]*spl[y]):
                                res.append('UNKNOWN')
                        else:
                                res.append(spl[y]-spl[x])
        print('#'+str(j+1), end=' ')
        for k in res:
                if k == res[-1]:
                        print(k)
                else:
                        print(k, end=' ')
