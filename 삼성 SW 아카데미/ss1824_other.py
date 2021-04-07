for tc in range(int(input())):
    ans = ''
    r, c = map(int, input().split())
    program=[list(input()) for _ in range(r)]
    maps = [[[] for _ in range(c)] for _ in range(r)]
 
    dy = [-1,0,1,0]; dx = [0,1,0,-1]
     
    d = 1; v = 0
    y = 0; x = 0
    q = [(y,x,d,v)]
    while q:
        (y,x,d,v) = q.pop()
         
        # 1. save direction and value
        maps[y][x].append((d,v))
         
        # 2. operate
        operation = program[y][x]
        if operation=='@':
            ans="YES"
            break
        elif operation=='?':
            for direction in range(4):
                ny = (y+dy[direction])%r; nx = (x+dx[direction])%c
                if not (direction,v) in maps[ny][nx]: q.append((ny,nx,direction,v))
            continue
        elif operation in ["<",">","^","v"]:
            if operation=="<": d=3
            elif operation==">": d=1
            elif operation=="^": d=0
            else: d = 2
        elif operation in ['_', '|']:
            if operation=='_' and v==0: d=1
            elif operation=='_' and v!=0: d=3
            elif operation=='|' and v==0: d=2
            else: d=0
        elif operation in ['+','-']:
            if operation=='+': v = (v+1)%16
            else: v = (v-1)%16
        elif operation in '0123456789':
            v = int(operation)
         
        ny = (y+dy[d])%r; nx = (x+dx[d])%c
        if not (d,v) in maps[ny][nx]: q.append((ny,nx,d,v))
 
     
    if ans=='': ans = 'NO'
    print('#{} {}'.format(tc+1, ans))
'''
#1 YES
#2 NO
#3 YES ----------------------
#4 YES
#5 YES
#6 YES
#7 NO
#8 NO
#9 YES
#10 YES
#11 YES
#12 YES
#13 YES ----------------------
#14 NO
#15 YES
#16 YES
#17 YES
#18 YES
#19 YES
#20 YES
#21 YES
#22 YES
#23 YES
#24 YES
#25 YES
#26 YES
#27 YES
#28 YES
#29 YES
#30 YES
#31 YES
#32 YES
#33 YES
#34 YES
#35 NO
#36 YES
#37 YES
#38 YES
#39 NO
#40 NO
#41 YES
#42 YES
#43 NO
#44 YES
#45 YES
#46 YES
#47 YES
#48 NO
#49 NO  --------------- ---------------
#53 YES
#54 YES
#55 YES
#56 YES
#57 NO-----------------
#58 YES
#59 YES
#60 NO
#61 YES
#62 YES----------------
#63 NO
#64 YES
#65 YES
#66 YES
#67 YES
#68 YES
#69 YES
'''
