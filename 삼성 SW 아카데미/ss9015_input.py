for ii in range(int(input())):
        item=int(input())
        a=input().split()
        for j in range(item):
                a[j]=int(a[j])
        count=1
        ind=0
        temp=[a.pop()]
        for i in range(len(a)):
                n=a.pop()
                if ind*(temp[-1]-n)<0:
                        temp=[n]
                        ind=0
                        count+=1
                else:
                        temp.append(n)
                        if len(temp)>1 and temp[-2]!=temp[-1]:
                                ind=temp[-2]-temp[-1]
        print('#'+str(ii+1),count)
