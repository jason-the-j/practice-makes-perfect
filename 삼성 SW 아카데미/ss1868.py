from collections import deque
vert=(1,1,1,-1,-1,-1,0,0)
hori=(1,-1,0,1,-1,0,1,-1)
def track(x):
        for ii in range(x,n):
                for jj in range(n):
                        if trap[ii][jj]=='.':
                                no=1                                     
                                for kk in range(8):
                                        a,b=ii+vert[kk],jj+hori[kk]
                                        if a>-1 and b>-1 and a<n and b<n:
                                                if trap[a][b]=='*':
                                                        no=0
                                                        break
                                if no:
                                        return ii,jj
def expand(x,y):
        arr=deque()
        arr.append([x,y])
        trap[x][y]=0
        while arr:
                e,s=arr.popleft()
                stop=0
                for kk in range(8):
                        a,b=e+vert[kk],s+hori[kk]
                        if a>-1 and b>-1 and a<n and b<n:
                                if trap[a][b]=='*':
                                        stop=1
                if not stop:
                        for kk in range(8):
                                a,b=e+vert[kk],s+hori[kk]
                                if a>-1 and b>-1 and a<n and b<n and trap[a][b]=='.':
                                        arr.append([a,b])
                                        trap[a][b]=0
                
for j in range(int(input())):
        n=int(input())
        trap=[[0]*n for _ in range(n)]
        for _ in range(n):
                tem=input()
                for __ in range(n):
                        trap[_][__]=tem[__]
        count=0
        init=track(0)
        while init!=None:
                expand(init[0],init[1])
                init=track(init[0])
                count+=1
        for i in range(n):
                for k in range(n):
                        if trap[i][k]=='.':
                                count+=1

        print('#'+str(j+1), count)
