def sixteentotwo(n):
        ans=str()
        div=8
        for i in range(4):
                if i<3:
                        ans+=str(n//div)
                        n=n%div
                        div=div//2
                else:
                        ans+=str(n%2)
        return ans

sixteen={'0':1,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
code={'0001101':'0','0011001':'1','0010011':'2','0111101':'3','0100011':'4','0110001':'5','0101111':'6', '0111011':'7', '0110111':'8','0001011':'9'}

for j in range(int(input())):
        check=[]
        m,n=map(int, input().split())
        for k in range(m):
                temp=str()
                random=input()
                for l in range(len(random)-1):
                        if random[l]!='0':
                                temp+=random[l]
                                if random[l+1]=='0':
                                        if temp not in check:
                                                check.append(temp)
                                        temp=str()

        total=0
        for z in check:
                binary=str()
                for y in z:
                        binary+=sixteentotwo(sixteen[y])
                ratio=len(binary)//56
                lenn=56*ratio
                if len(binary)!=56*ratio:
                        count=len(binary)
                        while count>lenn:
                                if binary[-1]=='0':
                                        binary=binary[:-1]
                                        count-=1
                                else:
                                        binary=binary[1:]
                                        count-=1
                print(binary)
                deci=''
                new=''
                for r in range(0,lenn,ratio):
                        new+=binary[r]
                
                for x in range(0,56,7):
                        deci+=code[new[x:x+7]]
                final=3*(int(deci[0])+int(deci[2])+int(deci[4])+int(deci[6]))+int(deci[1])+int(deci[3])+int(deci[5])+int(deci[-1])
                if not final%10:
                        summ=0
                        for d in deci:
                                summ+=int(d)
                        total+=summ
        print('#'+str(j+1),total)
