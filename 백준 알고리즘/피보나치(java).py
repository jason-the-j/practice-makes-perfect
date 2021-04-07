res=[0,1];
count=[[1,0],[0,1]]

def ad(a ,b):
        re=[];
        for i in range(2):
                c=a[i]+b[i];
                re.append(c)
        return re

for i in range(2,41):
        res.append(res[i-1]+res[i-2]);

for p in range(2,41):
        count.append(ad(count[p-1],count[p-2]));

n=int(input())
li=[];
for k in range(n):
        q=int(input())
        li.append(q);

for j in range(n):
        print(count[li[j]][0],count[li[j]][1])
       
