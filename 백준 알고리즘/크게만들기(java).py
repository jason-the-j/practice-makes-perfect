import sys
n, k = map(int, sys.stdin.readline().strip().split())
num=sys.stdin.readline().strip()
res=[]
for i in num:
        while k>0:
                if len(res)>0 and res[-1]<i:
                        b=res.pop()
                        k-=1
                else:
                        res.append(i)
                        break
        else:
                res.append(i)
print(''.join(res[:n-k]))
