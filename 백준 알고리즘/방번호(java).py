room=input();
reqnum=[0 ,0, 0, 0, 0, 0, 0, 0, 0, 0];
if int(room)==0:
        print(1);
else:

        for i in range(len(room)):
                a=room[i];
                anum= int(a);
                reqnum[anum]=reqnum[anum]+1;

                
        reqnum[6]=(reqnum[6]+reqnum[9])/2+0.5;
        reqnum=reqnum[:-1];
        print(int(max(reqnum)))
