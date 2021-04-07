import sys

popu=int(sys.stdin.readline().strip())
comp=sys.stdin.readline().strip().split()
line=[popu]*popu;

for i in range(popu-1):
        count=int(comp[i])
        for j in range(popu):
                if count==0 and line[j]==popu:
                        line[j]=i+1
                        break

                if line[j]==popu:
                        count-=1

res=''
for i in line:
        res+=(str(i)+' ')
print(res[:-1])
