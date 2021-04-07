def summer(checker, num, sett):
        global count
        global n
        if num==0 and checker==n:
                count+=1
       
        if checker<n:
                com=sett[checker];
                checker+=1
                summer(checker, num,  sett);
                summer(checker, num-com, sett);

args=input();
a, b= args.split();
n=int(a);
s=int(b);
listof=input();
interg=listof.split();
for i in range(n):
        interg[i]=int(interg[i]);
if s==0:
        count=-1;
else:
        count=0;
summer(0,s, interg)
print(count)
