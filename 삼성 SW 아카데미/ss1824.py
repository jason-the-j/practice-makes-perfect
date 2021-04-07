direc={'<':10,'>':11,'^':12,'v':13,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
path=((0,-1),(0,1),(-1,0),(1,0))
for j in range(int(input())):
        r,c=map(int, input().split())
        q=[[0,0,1,0]]
        check=[[[[0]*16 for _ in range(4)] for __ in range(c)] for ___ in range(r)]
        lan=[input() for _ in range(r)]
        ans=''
        print('#'+str(j+1), end=' ')
        while q:
                x,y,d,nu=q.pop()
                check[x][y][d][nu]=1
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
        else:
                ans='NO'
        print(ans)
'''
#1 YES
#2 NO
#3 YES
#4 YES
#5 YES
#6 YES
#7 NO
#8 NO
#9 YES
#10 YES
#11 YES
#12 YES
#13 YES
#14 NO
#15 YES
#16 YES
#17 YES
#18 YES
#19 YES
#20 YES
#21 YES
#22 YES
#23 YES
#24 YES
#25 YES
#26 YES
#27 YES
#28 YES
#29 YES
#30 YES
#31 YES
#32 YES
#33 YES
#34 YES
#35 NO
#36 YES
#37 YES
#38 YES
#39 NO
#40 NO
#41 YES
#42 YES
#43 NO
#44 YES
#45 YES
#46 YES
#47 YES
#48 NO
#49 NO
#50 YES
#51 NO
#52 YES
#53 YES
#54 YES
#55 YES
#56 YES
#57 NO
#58 YES
#59 YES
#60 NO
#61 YES
#62 YES
#63 NO
#64 YES
#65 YES
#66 YES
#67 YES
#68 YES
#69 YES
'''
