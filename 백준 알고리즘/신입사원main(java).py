import sys

def gen(case):
        for _ in range(case):
                cand=int(sys.stdin.readline().strip())
                new=[0]*cand;
                for i in range(cand):
                        resume, inter=map(int, sys.stdin.readline().strip().split())
                        new[resume-1]=inter;
                yield new
        
def greedy(new):
        count=1;
        compare=1;
        limit=new[0];
        while limit>1:
                if new[compare]<limit:
                        limit=new[compare];
                        count+=1;
                compare+=1;
                
        return count

if __name__=="__main__":
        case=int(sys.stdin.readline().strip())
        for p in gen(case):
                print(greedy(p));

