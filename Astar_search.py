import heapq

def astar_search(graph, start, goal):
    open_set = [(0, start, [])]         #priority queue

    while open_set:
        current_cost, current_node, path = heapq.heappop(open_set)

       
        if current_node == goal:        #if current nide is goal return it
            return path + [current_node]

        for neighbor, edge_info in graph[current_node].items():     #looking for adjacent nodes
            neighbor_cost = current_cost + edge_info['weight']
            heuristic = edge_info['heuristic']
            total_cost = neighbor_cost + heuristic

            heapq.heappush(open_set, (total_cost, neighbor, path + [current_node]))     #add neighbour to queue

    return None         #goal not found

def input_graph(graph):
    while True:
        node = input("Enter a node (or type 'done' to finish): ")
        if node == 'done':
            break

        adjacent_nodes_input = input(f"Enter adjacent nodes, their weights, and heuristic values for '{node}' (comma-separated, format: node1:weight1:heuristic1, node2:weight2:heuristic2): ")
        if adjacent_nodes_input.strip() == "":
            graph[node] = {}
        else:
            adjacent_nodes_info = adjacent_nodes_input.split(',')
            edge_info = {}
            for info in adjacent_nodes_info:
                adj_node, weight, heuristic = info.split(':')
                edge_info[adj_node.strip()] = {'weight': int(weight.strip()), 'heuristic': int(heuristic.strip())}

            graph[node] = edge_info

    print("Graph:", graph)

    return graph


def main():
    graph = {}
    graph = input_graph(graph)
    start_node = input("Starting node? ")
    goal_node = input("Goal node? ")
    result = astar_search(graph, start_node, goal_node)
    if result is None:
        print("The goal cannot be reached.")
    else:
        print(result, sep=',')
        
        
main()