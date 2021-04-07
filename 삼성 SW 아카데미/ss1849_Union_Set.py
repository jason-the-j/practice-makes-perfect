def find(x):
        if root[x]==x:
                return x
        load[x]+=load[root[x]]
        root[x]=find(root[x])
        return root[x]

def add(x,y,z):
        rootx=find(x)
        rooty=find(y)
        if rootx==rooty:
                return
        if leng[rootx]>leng[rooty]:
                y,x=x,y
                z=-z
                rooty,rootx=rootx,rooty
        leng[rooty]+=leng[rootx]
        leng[rootx]=0
        load[rootx]=load[y]-z-load[x]
        root[rootx]=rooty
        
for j in range(int(input())):
        n,m=map(int, input().split())
        res=[]
        root=[__ for __ in range(n+1)]
        load=[0]*(n+1)
        leng=[1]*(n+1)
        for _ in range(m):
                a=input().split()
                if len(a)>3:
                        add(int(a[1]),int(a[2]),int(a[3]))
                else:
                        x,y=map(int, a[1:])
                        if find(x)==find(y):
                                res.append(str(load[y]-load[x]))
                        else:
                                res.append('UNKNOWN')
        print('#'+str(j+1), ' '.join(res))
