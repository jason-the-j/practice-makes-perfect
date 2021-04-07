sixteen={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
code={'112':'0','122':'1','221':'2','114':'3','231':'4','132':'5','411':'6', '213':'7', '312':'8','211':'9'}

tc=int(input())
for j in range(1,tc+1):
        check=[]
        m,n=map(int, input().split())
        store=[input() for _ in range(m)]
        compare=''
        for nex in store:
                temp=''
                if nex==compare:
                        continue
                compare=nex
                for l in nex:
                        temp+=sixteen[l]
                
                a,b,c,ind=0,0,0,0
                num=''
                for i in range(4*n-1, -1, -1):
                        if not int(temp[i]):
                                if not ind:
                                        if not a*b*c:
                                                continue
                                        else:
                                                div=min(a,b,c)
                                                num+=code[str(a//div)+str(b//div)+str(c//div)]
                                                a,b,c,=0,0,0
                                                if len(num)==8:
                                                        if num not in check:
                                                                check.append(num)
                                                        num=''
                                else:
                                        b+=1
                        else:
                                if ind:
                                        c+=1
                                        if i>0 and not int(temp[i-1]):
                                                ind=0
                                else:
                                        a+=1
                                        if i>0 and not int(temp[i-1]):
                                                ind=1
        total=0
        for deci in check:
                final=int(deci[0])+int(deci[2])+int(deci[4])+int(deci[6])+3*(int(deci[1])+int(deci[3])+int(deci[5])+int(deci[-1]))
                if not final%10:
                        for i in deci:
                                total+=int(i)
        print('#'+str(j+1),total)
