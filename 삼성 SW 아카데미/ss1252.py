def coat(base):
        global res
        global total
        if base==1:
                for i in range(s):
                        for j in range(s):
                                if surface[i][j]:
                                        res+=str(i+1)+' '+str(j+1)+' 1 '
                                        total+=1
        else:
                for check in range(base*base, minn[base-2]-1,-1):
                        for i in range(s):
                                for j in range(s):
                                        if (i+base-1)<s and (j+base-1)<s:
                                                count=0
                                                temp=[]
                                                for ii in range(base):
                                                        for jj in range(base):
                                                                if surface[i+ii][j+jj]:
                                                                        count+=1
                                                                        temp.append([i+ii,j+jj])
                                                if count==check:
                                                        res+=str(i+1)+' '+str(j+1)+' '+str(base)+' '
                                                        total+=1
                                                        while temp:
                                                                x,y=temp.pop()
                                                                surface[x][y]=0

minn=[2,5]
for k in range(int(input())):
        res=''
        total=0
        s=int(input())
        n=int(input())
        surface=[[0]*s for _ in range(s)]
        emp=input().split()
        for _ in range(0, 2*n,2):
                surface[int(emp[_])-1][int(emp[_+1])-1]=1
        coat(3)
        coat(2)
        coat(1)
        print('#'+str(k+1), total, res)
