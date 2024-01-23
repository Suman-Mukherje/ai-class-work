
def dfs(visited, graph, node):   
    
    if node not in visited:
        print (node)
        push(visited,node)
        for neighbour in graph[node]:
            #node1=neighbour[0]
            #print(neighbour[0])
            dfs(visited, graph, neighbour[0])


def push(lst,value):
    lst.append(value)
    
def pop(lst):
    a=lst.pop()
         
#graph=graphconstruction()
def main():
    graph1 = {
    'A':[('B',2),('C',3),('D',1)],
    'B':[('E',3)],
    'C':[],
    'D':[('G',9),('H',2)],
    'E':[('F',8)],
    'F':[],
    'G':[('I',3)],
    'H':[],
    'I':[]
    }
    visited=[]
    dfs(visited, graph1, 'A')

main()

