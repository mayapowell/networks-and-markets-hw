
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
        self.edges = []
    
    def add_edge(self, nodeA, nodeB):
        ''' Adds an undirected edge to the graph, between nodeA and nodeB. Order of arguments should not matter'''

        if len(self.edges) == 0:
            self.edges.append([nodeA,nodeB])
            
        else:
            for i in self.edges: 
                if i[0]== nodeA or i[0] == nodeB:
                    if i[1] == nodeA or i[1] == nodeB:
                        pass
                    else: 
                        self.edges.append([nodeA,nodeB])
                else: 
                    self.edges.append([nodeA,nodeB])

    
       
    
    def edges_from(self, nodeA):
        ''' This method shold return a list of all the nodes nodeB such that nodeA and nodeB are 
        connected by an edge'''

        blist = []
        for i in self.edges: 
            if i[0]== nodeA:
                blist.append(i[1])
            elif i[1] == nodeA:
                blist.append(i[0])
        
        return blist  
    
    def check_edge(self, nodeA, nodeB):
        ''' This method should return true is there is an edge between nodeA and nodeB, and false otherwise'''
        if len(self.edges) == 0:
            return False
        
        else: 

            for i in self.edges: 
                if i[0]== nodeA or i[0] == nodeB:
                    if i[1] == nodeA or i[1] == nodeB:
                        return True
                    else: 
                        return False
                else:
                    return False

    
    def number_of_nodes(self):
        ''' This method should return the number of nodes in the graph'''
        return self._number_of_nodes
        


# Problem 9(a)
def create_graph(n,p):
    ''' Given number of nodes n and probability p, output an UndirectedGraph with n nodes, where each
    pair of nodes is connected by an edge with probability p'''

    graph = UndirectedGraph(n)

    for i in range(n):
        for j in range(n):
            threshold = rand.random()
            if i!=j:
                if threshold <= p:
                    graph.add_edge(i, j)

    return graph
    
    
# Problem 9(b)
def shortest_path(G,i,j):
    ''' Given an UndirectedGraph G and nodes i,j, output the length of the shortest path between i and j in G.
    If i and j are disconnected, output -1.'''
    if i == j:
        return 0
    
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
   
   
    """
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [i]
    #keeps track of the length of the shortest path between i and j in G
    counter = 0

    if i==j:
        return 0

 
    # keep looping until there are nodes still to be checked
    while queue:
        #add 1 to counter 
        counter += counter
        #check if this node is connected to our target node 
        if UndirectedGraph.check_edge(G,i,j):
            return counter
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
         # add node to list of checked nodes
        explored.append(node)
        neighbours = UndirectedGraph.edges_from(G,node)
 
        # add neighbours of node to queue
        for neighbour in neighbours:
            if node not in explored: 
                 queue.append(neighbour)

    return -1
    """

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




    # TODO: Implement this method 
    # for line in open(filename):
    #     pass
    pass

# Please include any additional code you use for analysis, or to generate graphs, here. This will be manually graded.
# Problem 9(c) if applicable.
# Problem 9(d)
# Problem 10(b)
# Problem 10(c) if applicable.
# Problem 10(d) if applicable.
def main():
    # TODO: Implement this method
    print("hello world")

if __name__ == "__main__":
    main()
