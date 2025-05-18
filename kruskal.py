inpt=[[1,2,1],[1,3,3],[2,6,4],[3,6,2],[3,4,1],[4,5,5],[7,5,7],[7,6,2],[6,5,6]]
n=7
answer=[]
inpt=sorted(inpt,key=lambda inpt:inpt[2])
graph=[-1]*(n+1)
def find(graph,node):
    if graph[node]<0:
        return node
    else:
        tmp=find(graph,graph[node])
        graph[node]=tmp
        return tmp
def union(graph,a,b,answer):
    ta=a
    tb=b
    a=find(graph,a)
    b=find(graph,b)
    
    if a==b:
        pass
    else:
        answer.append([ta,tb])
        if graph[a]==graph[b]:
            graph[a]=graph[a]+graph[b]
            graph[b]=a
        elif graph[a]<graph[b]:
            graph[a]=graph[a]+graph[b]
            graph[b]=a
        else:
            graph[b]=graph[a]+graph[b]
            graph[a]=b
            
cost=0

for u,v,d in inpt:
    union(graph,u,v,answer)
    cost+=d
for item in answer:
    print(item)
print(cost)