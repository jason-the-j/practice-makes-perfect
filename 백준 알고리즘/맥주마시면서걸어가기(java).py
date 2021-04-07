import collections as col
def happy(start, check, listof):
        q=col.deque([start]);
        while q:
                temp=q.popleft();
                count=0;
                for k in listof:
                        count+=1;
                        if check[count]==False and (abs(temp[0]-k[0])+abs(temp[1]-k[1]))<=1000:
                                if k==dest:
                                        return 'happy'
                                else:
                                        check[count]=1;
                                        q.append(k)
        return 'sad'


case=int(input());
for i in range(case):
        checker=list()
        convi=int(input());
        home=input().split(' ');
        home[0]=int(home[0]);
        home[1]=int(home[1]);
        checker.append(1);
        convilist=list();
        for j in range(convi):
                temp=input().split(' ');
                convilist.append([int(temp[0]), int(temp[1])]);
                checker.append(0);
        dest=input().split(' ');
        dest[0]=int(dest[0]);
        dest[1]=int(dest[1]);
        convilist.append(dest);
        checker.append(0);
        print(happy(home, checker, convilist))
