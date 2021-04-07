import collections as col

def dfs(i, visited, t):
        count=0;
        if i == t:
                return count

        else:
                
                visited[i]=1;
                queue =col.deque([i]);
                while queue:
                        count=count+1;
                        for m in range(len(queue)):
                                                       
                                temp=queue.popleft();
                                a, b, c= temp-1, temp+1, 2*temp;
                                listof=[a,b,c]
                                for k in listof:
                                        if k>=0 and k<=100000 and visited[k] ==0:
                                                if k == t:
                                                        return count
                                                else:
                                                        queue.append(k)
                                                        visited[k]=1;
        
args=input();
r, target = args.split();
visit=list();
for i in range(100001):
        visit.append(0);
 
print(dfs(int(r), visit, int(target)))
