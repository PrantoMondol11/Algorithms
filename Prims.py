from heapq import *


    
def prims(graph,start,parents,visited,distance):
    bag=[]
    heappush(bag,[0,start])
    parents[start]=-1
    distance[start]=0
    while bag:
        d,n=heappop(bag)
        if not visited[n]:
            visited[n]=1
            for cd,cn in graph[n]:
                if distance[cn]>cd and not visited[cn]:
                    distance[cn]=cd
                    parents[cn]=n
                    heappush(bag,[cd,cn])


input =[[1,2,7],[2,3,5],[3,5,2],[3,4,4],[5,4,1],[4,6,9],[6,8,12],[7,6,5],[3,7,3],[7,9,6],[8,9,10],[1,9,15]]
graph={}
parents={}
visited={}
distance={}

for i in range (1,10):
    parents[i]=None
    visited[i]=0
    distance[i]=10**8+1
    graph[i]=[]
    
for u,v,w in input:
    graph[u].append([w,v])
    graph[v].append([w,u])       
prims(graph,1,parents,visited,distance) 
print(parents) 
sum=0 
for i in distance.values():
    sum += i

print(sum)    
        