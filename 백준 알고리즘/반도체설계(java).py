import sys

port=int(sys.stdin.readline().strip())
link=sys.stdin.readline().strip().split()
for i in range(port):
        link[i]=int(link[i])

tail=[port+1]*port;
l=1
for i in range(port):
        if i == 0:
                tail[i]=link[i]
        else:
                base=0 # lo=base
                hi=l
                while hi-base>0: #base => index of tail changet
                        mid=(base+hi)//2
                        if tail[mid]<link[i]:
                                base=mid+1
                        else:
                                hi=mid

                if base==0:
                        if tail[base]>link[i]:
                                tail[base]=link[i]
                else:
                        if tail[base-1]<link[i] and tail[base]>link[i]:
                                tail[base]=link[i]
                if l==base:
                        l+=1

res=len(tail)
while tail[res-1]==port+1:
        res-=1
print(res)
        
