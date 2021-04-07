a=[]
n=1
k=1

def dist(start, dest):
        start=check(start)
        dest=check(dest)
        x,y=(dest[0]-start[0]),(dest[1]-start[1])
        if y<0:
                return x+start[1]-dest[1]
        elif y>x:
                return x+abs(x-y)
        else:
                return x

def check(num):
        for j in range(1,len(a)):
                if num <a[j]:
                        x=j
                        y=j-(a[j]-num)+1
                        break
        return [x,y]

while k<10013:
        k=n*(n-1)/2+1
        a.append(int(k))
        n+=1
        

for ii in range(int(input())):
        start, dest=map(int, input().split())
        print('#'+str(ii+1), dist(min(start,dest),max(start,dest)))
