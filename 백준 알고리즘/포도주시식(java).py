n=int(input())
wine=[];
for _ in range(n):
        l=int(input())
        wine.append(l);
        
res=[];
for i in range(n):
        if (i==0) or (i==1):
                res.append(sum(wine[:i+1]));

        elif i==2:
                res.append(sum(wine[:i+1])-min(wine[:i+1]));

        else:
                res.append(max(res[i-3]+wine[i-1]+wine[i], res[i-2]+wine[i], res[i-1]))

print(res[n-1])
        
