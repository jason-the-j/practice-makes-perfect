num=(input());
if num[0]=='0':
        print(0)
else:
        dp=[1,1];
        one=[1,1];
        ten=[0,0];

        for i in range(1,len(num)):
                if int(num[i-1:i+1])>9 and int(num[i-1:i+1])<27:
                        ten.append(dp[i-1]);
                else:
                        ten.append(0);

                if int(num[i])>0:
                        one.append(dp[i]);
                else:
                        one.append(0);

                dp.append(one[i+1]+ten[i+1]);
        print(dp[len(num)]%1000000)
