N=int(input())

res=[0,0,1,1];

for i in range(4,N+1):
        if i%3==0:
                res.append(min(res[i-1],res[int(i/3)])+1);
        elif i%2==0:
                res.append(min(res[i-1],res[int(i/2)])+1);

        else:
                res.append(res[i-1]+1);

print(res[N])

