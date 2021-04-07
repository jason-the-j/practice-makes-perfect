direc={'<':10,'>':11,'^':12,'v':13,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
path=((0,-1),(0,1),(-1,0),(1,0))
for j in range(int(input())):
        r,c=map(int, input().split())
        q=[[0,0,1,0]]
        check=[[[[0]*16 for _ in range(4)] for __ in range(c)] for ___ in range(r)]
        check[0][0][1][0]=1
        lan=[input() for _ in range(r)]
        ans=''
        print('#'+str(j+1), end=' ')
        while q:
                x,y,d,nu=q.pop()
                if lan[x][y]=='_':
                        if not nu:
                                d=1
                        else:
                                d=0
                elif lan[x][y]=='|':
                        if not nu:
                                d=3
                        else:
                                d=2
                elif lan[x][y]=='?':
                        for i in range(4):
                                g,h=path[i]
                                a,b=(x+g)%r,(y+h)%c
                                if not check[a][b][i][nu]:
                                        q.append([a,b,i,nu])
                                        check[a][b][i][nu]=1
                        continue
                elif lan[x][y]=='+':
                        nu=(nu+1)%16
                elif lan[x][y]=='-':
                        nu=(nu-1)%16
                elif lan[x][y]=='@':
                        ans='YES'
                        break
                else:
                        if lan[x][y]!='.':
                                if direc[lan[x][y]]>9:
                                        d=direc[lan[x][y]]-10
                                else:
                                        nu=direc[lan[x][y]]
                a,b=(x+path[d][0])%r,(y+path[d][1])%c
                if not check[a][b][d][nu]:
                        q.append([a,b,d,nu])
                        check[a][b][d][nu]=1
        else:
                ans='NO'
        print(ans)
