n=int(input())
val=[];
for _ in range(n):
        val.append(int(input()));
        
dp=[];
for i in range(n):
        if (i==0) or (i==1):
                dp.append(sum(val[:i+1]));

        elif i==2:
                dp.append(max(val[2]+val[1],val[0]+val[2]));

        else:
                dp.append(max(dp[i-2]+val[i],dp[i-3]+val[i-1]+val[i]))
                
print(dp[n-1])
