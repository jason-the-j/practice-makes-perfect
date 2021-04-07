from collections import deque
def path(start, dest):
        res=0
        if start*dest==1:
                return 0
        if depth[start]!=depth[dest]:
                if depth[start]>depth[dest]:
                        start=parent[start]
                else:
                        dest=parent[dest]
                res+=1
        while start!=dest:
                res+=2
                start,dest=parent[start],parent[dest]
        else:
                return res
for z in range(int(input())):
        n=int(input())
        q=deque()
        q.append(1)
        check=[0]*(n+1)
        check[0],check[1]=1,1
        parent, depth=[0,0],[0,0]
        route=[[] for i in range(n+1)]
        for i in input().split():
                parent.append(int(i))
        for i in range(2,n+1):
                if parent[i]==1:
                        depth.append(1)
                else:
                        depth.append(depth[parent[i]]+1)
                route[parent[i]].append(i)
        prev=1
        total=0
        while q:
                now=q.popleft()
                for j in route[now]:
                        if not check[j]:
                                check[j]=1
                                q.append(j)
                total+=path(prev,now)
                prev=now
        print('#'+str(z+1),total)
