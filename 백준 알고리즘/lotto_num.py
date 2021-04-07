import sys
from itertools import combinations
while True:
        inpu=sys.stdin.readline().split()
        for i in range(int(inpu[0])+1):
                inpu[i]=int(inpu[i])
        if inpu==[0]:
                break
        else: # length of S = test[0], s = test[1:]
                 com=combinations(inpu[1:],6)
                 for i in list(com):
                         for j in range(6):
                                 if j==5:
                                         print(i[j], end='\n')
                                 else:
                                         print(i[j],end=' ')
                 print('')
