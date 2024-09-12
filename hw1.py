
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
        self.number_of_nodes = number_of_nodes
        self.edges = []
    
    def add_edge(self, nodeA, nodeB):
        ''' Adds an undirected edge to the graph, between nodeA and nodeB. Order of arguments should not matter'''
        for i in self.edges: 
          if i[0]== nodeA or i[0] == nodeB
            if i[1] == nodeA or i[1] == nodeB
                pass
                else self.edges.append([nodeA,nodeB])
            else self.edges.append([nodeA,nodeB])
      
       
    
    def edges_from(self, nodeA):
        ''' This method shold return a list of all the nodes nodeB such that nodeA and nodeB are 
        connected by an edge'''
        
        pass
    
    def check_edge(self, nodeA, nodeB):
        ''' This method should return true is there is an edge between nodeA and nodeB, and false otherwise'''

        
        
        # TODO: Implement this method
        pass
    
    def number_of_nodes(self):
        ''' This method should return the number of nodes in the graph'''
        return self.number_of_nodes
        


# Problem 9(a)
def create_graph(n,p):
    ''' Given number of nodes n and probability p, output an UndirectedGraph with n nodes, where each
    pair of nodes is connected by an edge with probability p'''
    # TODO: Implement this method
    pass

# Problem 9(b)
def shortest_path(G,i,j):
    ''' Given an UndirectedGraph G and nodes i,j, output the length of the shortest path between i and j in G.
    If i and j are disconnected, output -1.'''
    # TODO: Implement this method
    pass

# Problem 9(c)
def avg_shortest_path(G, num_samples=1000):
    ''' Given an UndirectedGraph G, return an estimate of the average shortest path in G, where the average is taken
    over all pairs of CONNECTED nodes. The estimate should be taken by sampling num_samples random pairs of connected nodes, 
    and computing the average of their shortest paths. Return a decimal number.'''
    # TODO: Implement this method
    pass

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
