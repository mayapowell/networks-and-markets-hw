import numpy as np
import matplotlib.pyplot as plt
import random as rand




class UndirectedGraph:
    def __init__(self, number_of_nodes):
        ''' Assume that nodes are represented by indices/integers between 0 and number_of_nodes - 1. '''
        self._number_of_nodes = number_of_nodes
        self.adj_list = {i: set() for i in range(number_of_nodes)}  # Use a dictionary to store adjacency lists
    
    def add_edge(self, nodeA, nodeB):
        ''' Adds an undirected edge to the graph, between nodeA and nodeB. '''
        if nodeA != nodeB:  # Ignore self-loops
            self.adj_list[nodeA].add(nodeB)
            self.adj_list[nodeB].add(nodeA)
    
    def edges_from(self, nodeA):
        ''' Return a list of all nodes connected to nodeA by an edge. '''
        return list(self.adj_list[nodeA])
    
    def check_edge(self, nodeA, nodeB):
        ''' Return True if there is an edge between nodeA and nodeB, otherwise False. '''
        return nodeB in self.adj_list[nodeA]
    
    def number_of_nodes(self):
        ''' Return the number of nodes in the graph. '''
        return self._number_of_nodes


# Problem 9(b) - Optimize BFS in shortest_path
def shortest_path(G, i, j):
    ''' Given an UndirectedGraph G and nodes i,j, output the length of the shortest path between i and j in G.
        If i and j are disconnected, output -1. '''
    if i == j:
        return 0
    
    visited = [False] * G.number_of_nodes()  # Track visited nodes
    queue = [(i, 0)]  # BFS queue storing tuples of (node, distance)
    visited[i] = True
    
    while queue:
        current_node, distance = queue.pop(0)
        
        for neighbor in G.edges_from(current_node):
            if not visited[neighbor]:
                if neighbor == j:
                    return distance + 1  # Shortest path found
                visited[neighbor] = True
                queue.append((neighbor, distance + 1))
    
    return -1  # No path found if we exhaust the queue


# Problem 9(a) - This function already has good time complexity, but it's using rand.random()
# Let's make it a bit more Pythonic
def create_graph(n, p):
    ''' Given number of nodes n and probability p, output an UndirectedGraph with n nodes, 
        where each pair of nodes is connected by an edge with probability p. '''
    graph = UndirectedGraph(n)
    
    for i in range(n):
        for j in range(i + 1, n):
            if rand.random() <= p:
                graph.add_edge(i, j)
    
    return graph


# Problem 9(c) - No major changes needed here, the logic is solid. 
# This is a simulation function.
def avg_shortest_path(G, num_samples=1000):
    ''' Given an UndirectedGraph G, return an estimate of the average shortest path in G, 
        taken over all pairs of connected nodes, by sampling random pairs. '''
    total_distance = 0
    count = 0
    
    for _ in range(num_samples):
        i = rand.randint(0, G.number_of_nodes() - 1)
        j = rand.randint(0, G.number_of_nodes() - 1)
        
        distance = shortest_path(G, i, j)
        if distance != -1:
            total_distance += distance
            count += 1
    
    if count == 0:
        return -1  # No connected pairs found
    return total_distance / count


# Problem 10(a)
def create_fb_graph(filename="facebook_combined.txt"):
    ''' Return an undirected version of the Facebook graph as an instance of the UndirectedGraph class.
        You may assume the input graph has 4039 nodes. '''
    graph = UndirectedGraph(4039)  # Fixed number of nodes
    
    with open(filename, 'r') as file:
        for line in file:
            nodeA, nodeB = map(int, line.split())
            graph.add_edge(nodeA, nodeB)
    
    return graph




"""
graph9d1 = create_graph(1000,0.01)
print("step")
graph9d2 = create_graph(1000,0.02)
print("step")
graph9d3 = create_graph(1000,0.03)
print("step")
graph9d4 = create_graph(1000,0.04)
print("step")
graph9d5 = create_graph(1000,0.05)
print("step")
graph9d6 = create_graph(1000,0.1)
print("step")
graph9d7 = create_graph(1000,0.15)
print("step")
graph9d8 = create_graph(1000,0.2)
print("step")
graph9d9 = create_graph(1000,0.25)
print("step")
graph9d10 = create_graph(1000,0.3)
print("step")
graph9d11 = create_graph(1000,0.35)
print("step")
graph9d12 = create_graph(1000,0.4)
print("step")
graph9d13 = create_graph(1000,0.45)
print("step")
graph9d14 = create_graph(1000,0.5)
print("step")

av1 = (avg_shortest_path(graph9d1, num_samples=1000))
print("step")
av2 = (avg_shortest_path(graph9d2, num_samples=1000))
print("step")
av3 = (avg_shortest_path(graph9d3, num_samples=1000))
print("step")
av4 = (avg_shortest_path(graph9d4, num_samples=1000))
print("step")
av5 = (avg_shortest_path(graph9d5, num_samples=1000))
print("step")
av6 = (avg_shortest_path(graph9d6, num_samples=1000))
print("step")
av7 = (avg_shortest_path(graph9d7, num_samples=1000))
print("step")
av8 = (avg_shortest_path(graph9d8, num_samples=1000))
print("step")
av9 = (avg_shortest_path(graph9d9, num_samples=1000))
print("step")
av10 = (avg_shortest_path(graph9d10, num_samples=1000))
print("step")
av11 = (avg_shortest_path(graph9d11, num_samples=1000))
print("step")
av12 = (avg_shortest_path(graph9d12, num_samples=1000))
print("step")
av13 = (avg_shortest_path(graph9d13, num_samples=1000))
print("step")
av14 = (avg_shortest_path(graph9d14, num_samples=1000))
print("step")

plist = [0.01, 0.02, 0.03, 0.04, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
averagedist = [av1, av2, av3, av4, av5, av6, av7, av8, av9, av10, av11, av12, av13, av14]

plt.xlabel("Probability")
plt.ylabel("Average Distance Betwwen Nodes")
plt.plot(plist, averagedist)
plt.draw()
plt.show()




FbGraph = create_fb_graph("facebook_combined.txt")
print(avg_shortest_path(FbGraph, num_samples=1000))

"""

graph10d = create_graph(4039,0.01081)
print(avg_shortest_path(graph10d, num_samples=1000))