for j in range(int(input())):
        n,score=int(input()),input().split()
        for _ in range(n):
                score[_]=int(score[_])
        check=[0]*10001
        check[0]=1
        res=[0]
        for i in score:
                for k in range(len(res)):
                        if not check[res[k]+i]:
                                check[res[k]+i]=1
                                res.append(res[k]+i)
        print('#'+str(j+1),len(res))
