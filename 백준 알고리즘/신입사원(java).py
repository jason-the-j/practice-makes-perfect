import sys

for _ in range(int(input())):
        cand=int(sys.stdin.readline().strip())
        new=[0]*cand;
        for i in range(cand):
                resume, inter=map(int, sys.stdin.readline().strip().split())
                new[resume-1]=inter;
                
        count=1;
        compare=1;
        limit=new[0];
        while limit>1:
                if new[compare]<limit:
                        limit=new[compare];
                        count+=1;
                compare+=1;
                
        print(count);
