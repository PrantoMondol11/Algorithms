class graph:
    def __init__(self,directed,weighted):
        self.directed=directed
        self.weighted=weighted
        self.dict={}
    
    def  addNode(self,nodeName):
        if nodeName not in self.dict:
            self.dict[nodeName]=[]
        else:
            return "This node name already exists...."
    def addEdge(self,node1,node2,weight):
        if node1 not in self.dict:
            return node1+"is not in our graph"
        if node2 not in self.dict:
            return node2 + "is not inn our graph"
        self.dict[node1].append((node2,weight))
        if self.directed==False:
            self.dict[node2].append((node1,weight))

gp=graph(False,True)
gp.addNode("A")
gp.addNode("B")
gp.addNode("C")
gp.addNode("D")
gp.addNode("E")

gp.addEdge("A","B",5)
gp.addEdge("A","C",3)
gp.addEdge("B","C",7)
gp.addEdge("B","D",19)
gp.addEdge("B","E",2)
gp.addEdge("C","D",10)
gp.addEdge("D","E",8)

for key,value in gp.dict.items():
    print(key,end=(" "))
    for tuple in value:
        print(str(tuple[0])+" "+ str(tuple[1]),end=(" "))
    print()