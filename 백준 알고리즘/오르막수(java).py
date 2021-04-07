n=int(input())
dp=[]
step=[]
for i in range(n):
        if i ==0:
                dp.append(10);
                step.append([1,1,1,1,1,1,1,1,1]);
        else:
                temp=[]
                for j in range(9):
                        temp.append(sum(step[i-1][j:]));
                step.append(temp)
                dp.append(dp[i-1]+sum(step[i]))

print(dp[n-1]%10007)
