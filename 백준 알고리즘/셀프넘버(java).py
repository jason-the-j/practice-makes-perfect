def notself(n):
        res=n;
        while n>9:
                res+=n%10
                n=n//10
        res+=n
        return res


num=[]
for i in range(1,10001):
        num.append(i)

for i in range(1,10001):
        if i in num:
                i=notself(i);
                while i<10001 and i in num:
                        num.pop(num.index(i));
                        i=notself(i);

for i in num:
        print(i)

