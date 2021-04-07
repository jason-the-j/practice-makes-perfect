import sys

num=int(sys.stdin.readline().strip())
rope=[]
for i in range(num):
        rope.append(int(sys.stdin.readline().strip()))

rope.sort()
maxi=0
for j in range(num):
        maxi=max((len(rope)-j)*rope[j],maxi)

print(maxi)
