mn=input().split(' ');
for _  in range(2):
        mn[_]=int(mn[_]);

start=1;
dist=[0];
for i in range(int(input())):
        nex=int(input());
        if nex<start:
                dist.append(start-nex);
                start=nex

        elif nex>start+mn[1]-1:
                dist.append(nex-(start+mn[1]-1))        
                start=nex-(mn[1]-1);

print(sum(dist))
