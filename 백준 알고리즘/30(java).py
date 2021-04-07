import sys

number=sys.stdin.readline().strip()
num=[]
for i in number:
        num.append(i);
num.sort(reverse=True)
res=''
for j in num:
        res+=j

if int(res)%30==0:
        print(int(res))

else:
        print(-1)

