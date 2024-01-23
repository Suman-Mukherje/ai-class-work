    
def bfs(visited, graph, node): 
  visited = [] 
  queue = []
  enqueue(visited,node)
  enqueue(queue,node)
  

  while queue:          
    m = deque(queue) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        enqueue(visited,neighbour)
        enqueue(queue,neighbour)
        


def enqueue(lst,value):
    lst.append(value)
    
    
def deque(lst):
    a=lst.pop(0)
    return a 
    
def main():
    visited=[]
    graph1 = {
    'A':['B','C','D'],
    'B':['E'],
    'C':[],
    'D':['G','H'],
    'E':['F'],
    'F':[],
    'G':[],
    'H':[]
    }
    print("Following is the Breadth-First Search")
    bfs(visited, graph1, 'A')

main()
