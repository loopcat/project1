import numpy as np

# build adjacency matrix
# input: number of nodes
#        number of edges (not using right now but will need later)
#        paths
def build_matrix(n,e,paths):

    # initialize matrix to zeros (row and column 0 will not be used, just 1 to number of nodes)
    graphMatrix = np.zeros([n+1,n+1], dtype = int)

    # read paths and update matrix
    for x, y in paths:
        i = x
        j = y
        graphMatrix[i,j] = 1

    print(graphMatrix)


#==============
# driver

n = 4   # number of nodes
e = 5   # number of edges
paths = [(1,2), (2,4), (3,1), (3,4), (4,2)] # paths in directed graph
build_matrix(n, e, paths)

#--------------------------------------------------------------------------------------

# depth first search

# breadth first search