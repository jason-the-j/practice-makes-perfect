import sys

def search(now, limit, length, count, check):
        if check==count:
                print(length)
        else:
                for i in range(now+1,limit+2):
                        tem=length+' '+inpu[i]
                        search(i,limit+1,tem,count, check+1)

while True:
        inpu=sys.stdin.readline().split()
        if inpu==['0']:
                break
        else:
                for k in range(1,int(inpu[0])-4):
                        search(k, int(inpu[0])-5, inpu[k],6,1)
        print('')
