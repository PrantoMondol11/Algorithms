from heapq import *
inpt=[[1,3,2],[1,2,1],[2,3,1],[2,5,1],[3,4,2],[5,4,5]]
n=5
graph={}
distance={}
visited={}

def dijkstra(graph,start,visited,distance):
    distance[start]=0
    bag=[]
    heappush(bag,[0,start])
    while bag:
        d,n =heappop(bag)
        visited[n]=1
        for cd,cn in graph[n]:
            if not visited[cn] and distance[n]+cd<distance[cn]:
                distance[cn]=distance[n]+cd
                heappush(bag,[distance[n]+cd,cn])
                

for i in range(1,n+1):
    graph[i]=[]
    distance[i]=10**8+1
    visited[i]=0
    
for u,v,d in inpt:
    graph[u].append([d,v])
print(graph)

start=1
dijkstra(graph,start,visited,distance)
print(distance)