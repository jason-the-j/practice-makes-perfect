def make_set(x):
    global p,tab
    p[x]=x
    tab[x]=0
def find_set(x):
    global p,tab
    if x==p[x]:
        return x
    tab[x]+=tab[p[x]]
    print(tab)
    p[x] = find_set(p[x])
    return p[x]
def union(x,y,w):
    global p, c, tab, rank
    px = find_set(x)
    py = find_set(y)
    if px == py: return
    if rank[px]<=rank[py]:
        p[px]=py
        tab[px]=tab[y]-tab[x]-w
    else:
        p[py]=px
        tab[py]=tab[x]-tab[y]+w
    if rank[px]==rank[py]: rank[py]+=1
    find_set(x)
    find_set(y)
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    print("#%d"%tc, end=" ")
    p=[0]*(N+1)
    tab = [-1]*(N+1) #N x N (0은 안씀)
    rank=[0]*(N+1)
    for_prt=[]
    for m in range(M):
        line = input().split()
        if line[0]=='!':#정보제공
            a, b, w = map(int,line[1:])
            if not p[a]: make_set(a)
            if not p[b]: make_set(b)
            union(a, b, w)
        elif line[0]=='?':#질문
            a, b = map(int,line[1:])
            pa = find_set(a)
            pb = find_set(b)
            if pa==pb: for_prt.append(str(tab[b]-tab[a]))
            else: for_prt.append("UNKNOWN")
    print(" ".join(for_prt))
