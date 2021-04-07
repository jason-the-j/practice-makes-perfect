def change(ar):
        for _ in range(3):
                ar[_]=int(ar[_]);
        return ar

guide=change(input().split(' '));
route=[]
for s in range(guide[0]+1):
        te=[];
        for r in range(guide[0]+1):
                te.append(0);
        route.append(te);
        
for e in range(guide[2]):  #route- 0: start 1: destination 2:value / for guide 0:final 1:count 2:rout num
        k=change(input().split(' '));
        if k[0]<k[1]:
                route[k[0]][k[1]]=max(route[k[0]][k[1]],k[2]);

dp=[]
for z in range(guide[0]+1):
        tem=[];
        for w in range(guide[1]+1):
                tem.append(0);
        dp.append(tem);


dp[1][1]=1; # start point
for i in range(1,guide[0]):
        count=0; # route end point checker
        for j in route[i]: # route start point i end:count value:j
                if j!=0:
                        for a in range(guide[1]):
                                if dp[i][a]!=0:
                                        dp[count][a+1]=max(dp[count][a+1],dp[i][a]+j);
                count+=1

print(max(dp[guide[0]])-1); 
