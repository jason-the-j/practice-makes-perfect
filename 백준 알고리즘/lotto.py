import sys
from itertools import combinations
while True:
        inpu=sys.stdin.readline().split()
        if inpu==['0']:
                break
        else:                
                com=combinations(inpu[1:],6)
                for i in list(com):
                        print(' '.join(map(str,i)))
                print('')
