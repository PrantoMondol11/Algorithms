inpt=[[1,2,2],[1,3,1],[2,3,-2],[2,4,2],[3,5,-1]]
n=5
distance={}
for i in range(1,n+1):
    distance[i]=10**8+1

start=1
distance[start]=0

for _ in range(n-1):
    for u,v,d in inpt:
        if distance[u]<10**8 and d+distance[u]<distance[v]:
            distance[v]=d+distance[u]

print(distance)