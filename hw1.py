
# CS5854 HW1.py
# IMPORTANT: Please read all comments!

# ==========Collaborators=============
# Please enter here the netids of all members of your group (yourself included.)
# Groups are at maximum 3 people.
# You may submit the same python code, or you may choose to each submit 
# your own code on gradescope (in which case your submission will be 
# graded separately). But as long as you collaborate -- even a little bit -- 
# please put your collaborator's netids here so that we can track groups.
# ====================================
authors = ['drs374', 'mlp267']

# ==========Python Version============
# Which version of python are you using? 
# "Python 2" or "Python 3"? (Autograder defaults to 3) 
# ====================================
python_version = "3.12"

# ======Submission and Packages=======
# Make sure to submit hw1.py to Gradescope, and make
# sure to keep the name the same. If your code spans
# multiple files, upload all of them. You do not
# need to submit facebook_combined.txt. 
# Our autograder only supports the following external
# packages:
# [numpy, pandas, scipy, matplotlib, random]
# please contact us before submission if you want another 
# package approved, if reasonable.
# ====================================
import numpy as np
import matplotlib.pyplot as plt
import random as rand



# =====================================
# IMPORTANT: You are NOT allowed to modify the method signatures 
# (i.e. the arguments and return types each function takes). 
# But feel free to add other methods and attributes as needed. 
# We will pass your grade through an autograder which expects a specific 
# interface.
# =====================================
class UndirectedGraph:
    def __init__(self,number_of_nodes):
        '''Assume that nodes are represented by indices/integers between 0 and number_of_nodes - 1.'''
        self._number_of_nodes = number_of_nodes
        self.adj_list = {i: set() for i in range(number_of_nodes)}  # Dictionary to store adjacency lists
    
    def add_edge(self, nodeA, nodeB):
        ''' Adds an undirected edge to the graph, between nodeA and nodeB. Order of arguments should not matter'''

        if nodeA != nodeB:  # Ignore self-loops
            self.adj_list[nodeA].add(nodeB) #Add edge to both node dictionaries
            self.adj_list[nodeB].add(nodeA)
    
    def edges_from(self, nodeA):
        ''' This method shold return a list of all the nodes nodeB such that nodeA and nodeB are 
        connected by an edge'''

        return list(self.adj_list[nodeA]) #Returns all nodes that are in nodeA dictionary
    
    def check_edge(self, nodeA, nodeB):
        ''' This method should return true if there is an edge between nodeA and nodeB, and false otherwise'''
        return nodeB in self.adj_list[nodeA] #Returns T/F

    def number_of_nodes(self):
        ''' This method should return the number of nodes in the graph'''
        return self._number_of_nodes
        


# Problem 9(a)
def create_graph(n,p):
    ''' Given number of nodes n and probability p, output an UndirectedGraph with n nodes, where each
    pair of nodes is connected by an edge with probability p'''

    graph = UndirectedGraph(n)

    for i in range(n):
        for j in range(i + 1, n):
            threshold = rand.random()
            if i!=j and threshold <= p:
                graph.add_edge(i, j)

    return graph
    
# Problem 9(b)
def shortest_path(G,i,j):
    ''' Given an UndirectedGraph G and nodes i,j, output the length of the shortest path between i and j in G.
    If i and j are disconnected, output -1.'''
    if i == j:
        return -1 #comparing same node, return -1
    
    visited = [False] * G.number_of_nodes()  # Keep track of visited nodes
    queue = [(i, 0)]  # List to hold (node, current_distance)
    visited[i] = True  #Visited starting node
    
    while queue:
        current_node, distance = queue.pop(0)
        
        # Check all neighbors of the current node
        for neighbor in G.edges_from(current_node):
            if not visited[neighbor]:
                if neighbor == j:
                    return distance + 1  # Return the shortest path when we find node j
                visited[neighbor] = True
                queue.append((neighbor, distance + 1))  # Append to the end with updated distance
    
    return -1  # Return -1 if no path is found   
   

# Problem 9(c)
def avg_shortest_path(G, num_samples=1000):
    ''' Given an UndirectedGraph G, return an estimate of the average shortest path in G, where the average is taken
    over all pairs of CONNECTED nodes. The estimate should be taken by sampling num_samples random pairs of connected nodes, 
    and computing the average of their shortest paths. Return a decimal number.'''
        
    total_distance = 0
    count = 0
    
    for dummy in range(num_samples):

        i = rand.randint(0, G.number_of_nodes() - 1) #random int from 0 to (G.count - 1)
        j = rand.randint(0, G.number_of_nodes() - 1) 

        distance = shortest_path(G, i, j)
        
        if distance != -1:
            total_distance += distance
            count += 1
    
    if count == 0:
        return -1  # No connected pairs
    return total_distance / count #decimal value of average shortest path

# Problem 10(a)
def create_fb_graph(filename = "facebook_combined.txt"):
    ''' This method should return a undirected version of the facebook graph as an instance of the UndirectedGraph class.
    You may assume that the input graph has 4039 nodes.''' 

    graph = UndirectedGraph(4039)  # Create a graph with 4039 nodes
    
    with open(filename, 'r') as file:
        for line in file:
            nodeA, nodeB = map(int, line.split())  # Split the line into two integers
            graph.add_edge(nodeA, nodeB)  # Add the edge to the graph between nodes
    
    return graph

# Please include any additional code you use for analysis, or to generate graphs, here. This will be manually graded.


# Problem 9(c)
"""
graph9c = create_graph(1000,0.1)
print(avg_shortest_path(graph9c, num_samples=1000))
"""

# Problem 9(d)

"""
graph9d1 = create_graph(1000,0.01)
graph9d2 = create_graph(1000,0.02)
graph9d3 = create_graph(1000,0.03)
graph9d4 = create_graph(1000,0.04)
graph9d5 = create_graph(1000,0.05)
graph9d6 = create_graph(1000,0.1)
graph9d7 = create_graph(1000,0.15)
graph9d8 = create_graph(1000,0.2)
graph9d9 = create_graph(1000,0.25)
graph9d10 = create_graph(1000,0.3)
graph9d11 = create_graph(1000,0.35)
graph9d12 = create_graph(1000,0.4)
graph9d13 = create_graph(1000,0.45)
graph9d14 = create_graph(1000,0.5)

av1 = (avg_shortest_path(graph9d1, num_samples=1000))
av2 = (avg_shortest_path(graph9d2, num_samples=1000))
av3 = (avg_shortest_path(graph9d3, num_samples=1000))
av4 = (avg_shortest_path(graph9d4, num_samples=1000))
av5 = (avg_shortest_path(graph9d5, num_samples=1000))
av6 = (avg_shortest_path(graph9d6, num_samples=1000))
av7 = (avg_shortest_path(graph9d7, num_samples=1000))
av8 = (avg_shortest_path(graph9d8, num_samples=1000))
av9 = (avg_shortest_path(graph9d9, num_samples=1000))
av10 = (avg_shortest_path(graph9d10, num_samples=1000))
av11 = (avg_shortest_path(graph9d11, num_samples=1000))
av12 = (avg_shortest_path(graph9d12, num_samples=1000))
av13 = (avg_shortest_path(graph9d13, num_samples=1000))
av14 = (avg_shortest_path(graph9d14, num_samples=1000))

plist = [0.01, 0.02, 0.03, 0.04, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
averagedist = [av1, av2, av3, av4, av5, av6, av7, av8, av9, av10, av11, av12, av13, av14]


plt.xlabel("Probability")
plt.ylabel("Average Distance Betwwen Nodes")
plt.plot(plist, averagedist)
plt.draw()
plt.show()

"""


# Problem 10(b)
"""
FbGraph = create_fb_graph("facebook_combined.txt")
print(avg_shortest_path(FbGraph, num_samples=1000))
"""



# Problem 10(d)

graph10d = create_graph(4039,0.01081)
print(avg_shortest_path(graph10d, num_samples=1000))
