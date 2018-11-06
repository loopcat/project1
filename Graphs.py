import numpy as np

# build adjacency matrix
# input: number of nodes
#        number of edges (not using right now but will need later)
#        paths
def build_matrix(n,paths):

    # initialize matrix to zeros
    graphMatrix = np.zeros([n+1,n+1], dtype = int)

    # read paths and update matrix
    for x, y in paths:
        i = x
        j = y
        graphMatrix[i,j] = 1

    #print(graphMatrix)
    return graphMatrix

def depth_first_search(graphMatrix, node, n):
    # iterative algorithm
    nodeStack = []
    visited = [False for x in range(n + 1)]

    # for this node:  push to stack and mark as visited
    nodeStack.append(node)
    visited[node] = True

    # while stack is not empty
    while nodeStack:
        nextNode = nodeStack.pop()   # pop next node from top of stack

        # push all of nodes neighbors on the stack if they have not been visited
        for i in range(n+1):
            if graphMatrix[nextNode,i] == 1:
                if visited[i] == False:
                    nodeStack.append(i)
        visited[nextNode] = True
        print("Visited Vertex: ", nextNode)

    print(visited)



#==============
# driver

#      1
#     / \
#    2   3
#   / \
#  4   5
n = 5   # number of nodes
e = 4   # number of edges
paths = [(1,2), (1,3), (2,1), (2,4), (2,5), (3,1), (4,2), (5,2)] # paths in undirected graph
graphMatrix = build_matrix(n, paths)
print(graphMatrix)

# input: Graph, node to start, number of nodes
depth_first_search(graphMatrix, 1, n)




#--------------------------------------------------------------------------------------
