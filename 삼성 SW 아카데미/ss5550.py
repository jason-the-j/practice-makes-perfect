from collections import deque
rest={'r':1,'o':2,'a':3}
for j in range(int(input())):
        maxx,temp=0,0
        stack=deque()
        print('#'+str(j+1), end=' ')
        for i in input():
                stop=0
                if i=='c':
                        stack.append(1)
                        temp+=1
                        maxx=max(maxx,temp)
                else:
                        if not stack:
                                stop=1
                        else:
                                if i=='k':
                                        stack[0]+=1
                                        if stack.popleft() == 5:
                                                temp-=1
                                        else:
                                                stop=1
                                else:
                                        for k in range(temp):
                                                if stack[k]==rest[i]:
                                                        stack[k]+=1
                                                        break
                                                if k==temp-1:
                                                        stop=1
                if stop:
                        stack=1
                        break
        if stack:                     
                print(-1)
        else:
                print(maxx)
