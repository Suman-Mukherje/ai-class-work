# Implement graph in python
''' {0:[(1,5),(2,3)],
1:[(3,2),(4,15)],
2:[],
3:[],
4:[(2,7),(3,11)]
} '''

def graphconstruction(nodes):

    graph={}
    for n in nodes:
        adjacentlist=[]
        no=int(input("Enter no of the connected nodes with "+ n+":"))
        for i in range(no):
            adj = str(input("Enter the adjacent node"))
            weight=int(input("Enter the weight with that node"))
            adjacentlist.append((adj,weight))
        graph[n]= adjacentlist

    return graph

nodes=[]
non=int(input("Enter the no of nodes in your graph:"))
for i in range(non):
    node=input("Enter the node")
    nodes.append(node)
print(nodes)
print(graphconstruction(nodes))
