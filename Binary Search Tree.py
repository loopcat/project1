# binary search tree

# define tree node (tnode) with left & right pointers
class tnode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

# class binary search tree
class bst:
    def __init__ (self):
        self.root = None

    # search for a key (without recursion)
    def find(self, value):
        if self.root == None:
            return False

        else:
            curNode = self.root
            while curNode != None:
                if value == curNode.value:
                    return True
                else:
                    if value < curNode.value:
                        curNode = curNode.left
                    else:
                        curNode = curNode.right

            return False

    # find maximum key from given starting node (a non-empty BST)
    def find_max(self, curNode):

        while curNode != None:
            # if this is the last node get the key
            if curNode.right == None:
                maxKey = curNode.value

            # keep going right
            curNode = curNode.right

        return maxKey

    # find minimum key from given starting node(a non-empty BST)
    def find_min(self, curNode):

        while curNode != None:
            # if this is the last node, get the key
            if curNode.left == None:
                minKey = curNode.value

             # keep going left
            curNode = curNode.left

        return minKey

    # find the next largest value of key (in order traversal), input key and root node
    #   if the right subtree is not null the successor is the minimum key in the right subtree
    #   if the right subtree is null the successor is an ancestor.  Start with the root and travel
    #     down the tree to find the successor
    def in_order_successor(self, curNode, key):

        # check for empty tree
        if curNode == None:
            return

        # traverse the tree to find the node with the key and get the successor
        while curNode != None:
            if key == curNode.value:
                # if the node has a right subtree the successor is the min value from that subtree
                if curNode.right != None:
                    successor = self.find_min(curNode)
                    return successor

                # if the node does not have a right subtree start at the root and search for the successor.
                # each time there is a node with a value greater than the key it becomes the new successor
                if curNode.right == None:
                    curNode = root
                    while curNode != None:
                        if key < curNode.value:
                            successor = curNode.value
                            curNode = curNode.left
                        elif key > curNode.value:
                            curNode = curNode.right
                        else:
                            return successor
            else:
                # move down the tree to find the node with the key
                if key < curNode.value:
                    curNode = curNode.left
                else:
                    curNode = curNode.right

    # find predecessor of key (in order traversal), input key and root node
    #  if the left subtree is not null the predecessor is the max key in the left subtree
    #  if the left subtree is null the predecessor is an ancestor.  Start with root and travel
    #    down the tree to find the predecessor

    def in_order_predecessor(self, curNode, key):
        # check for empty tree
        if curNode == None:
            return

        # traverse the tree to find the node with the key and get the predecessor
        while curNode != None:
            if key == curNode.value:
                # if the node has a left subtree the predecessor is the max key in that subtree
                if curNode.left != None:
                    predecessor = self.find_max(curNode)
                    return predecessor

                # if the node does not have a left subtree start at the root and search for the predecessor.
                # each time there is a node with a value less than the key it becomes the new predecessor
                curNode = root
                while curNode != None:
                    if key < curNode.value:
                        curNode = curNode.left
                    elif key > curNode.value:
                        predecessor = curNode.value
                        curNode = curNode.right
                    else:
                        return predecessor

            else:
                # move down the tree to find the key
                if key < curNode.value:
                    curNode = curNode.left
                else:
                    curNode = curNode.right


    # find height of the tree:  h(node) = max{height(left child), height(right child} + 1
    def height(self,curNode):
        if curNode == None:
            return 0
        else:
            lheight = self.height(curNode.left)
            rheight = self.height(curNode.right)
            return max(lheight, rheight) + 1


    # insert a node
    def insert(self, value):
        # if root is null (empty tree), make this the root
        if self.root == None:
            self.root = tnode(value)
        else:
            self.insert_node(self.root, value)

    # recursive logic to actually insert the node
    def insert_node(self, curNode, value):
        if value < curNode.value:
            if curNode.left == None:
                curNode.left = tnode(value)
            else:
                self.insert_node(curNode.left, value)
        elif value > curNode.value:
            if curNode.right == None:
                curNode.right = tnode(value)
            else:
                self.insert_node(curNode.right, value)
        else:
            print("Can not insert a duplicate valuel")

    # print all keys in the tree
    def print_tree(self):
        if self.root == None:
            print("Empty Tree")
        else:
            self.print_tree_node(self.root)

    def print_tree_node(self, curNode):
        if curNode != None:
            self.print_tree_node(curNode.left)
            print("Node: ", curNode.value)
            self.print_tree_node(curNode.right)

    # print the root
    def print_root(self):
        if self.root == None:
            print("Empty Tree")
        else:
            print("Root: ", self.root.value)

#=======================
# driver code for BST
#=======================

myTree = bst()

# tree example 1
#myTree.insert(10)
#myTree.insert(5)
#myTree.insert(13)
#myTree.insert(3)
#myTree.insert(6)
#myTree.insert(12)
#myTree.insert(20)
#myTree.insert(1)

# tree example 2
myTree.insert(15)
myTree.insert(6)
myTree.insert(18)
myTree.insert(3)
myTree.insert(7)
myTree.insert(2)
myTree.insert(4)
myTree.insert(13)
myTree.insert(9)
myTree.insert(17)
myTree.insert(20)

# assign root
root = myTree.root
myTree.print_root()

# find the successor of key (in order traversal)
key = 9
succ = None
succ = myTree.in_order_successor(root, key)
if succ == None:
    print("No Successor")
else:
    print("Successor of key: ",key," -> ",succ)

# find the predecessor of the key
pred = None
pred = myTree.in_order_predecessor(root, key)
if pred == None:
    print("No Predecessor")
else:
    print("Predecessor of key: ", key, " -> ", pred)

# find minimum key in the tree
#print("Minimum Key: ", myTree.find_min(root))

# find maximum key in the tree
#print("Maximum Key: ",myTree.find_max(root))

# find if key exists in the tree
#key = 16
#print("Find: ", myTree.find(16))

# print all keys in the tree
#myTree.print_tree()

# find the tree height
#treeHeight = myTree.height(root)
#print("Tree height: ", treeHeight)




