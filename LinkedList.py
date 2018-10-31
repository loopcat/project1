# single linked list implementation

class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linked_list:

    # define head
    def __init__(self):
        self.head = None

    # insert a node at beginning of the list
    def insert_front(self, data):
        new_node = node(data)

        # set head pointer
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # delete a node
    def delete_node(self, data):
        temp = self.head
        prev = None

        # check if list is empty
        if temp is not None:
            # check if the head node is the one to be deleted
            if temp.value == data:
                self.head = temp.next
                temp = None
                return True

            # search for node to delete
            # use a prev pointer to track one node behind so we can do the delete
            while (temp):
                if temp.value == data:
                    prev.next = temp.next
                    return True

                prev = temp
                temp = temp.next

            # if node is not found
            if temp.next == None:
                return False

    # search
    def search(self,find):
        temp = self.head

        # is list empty
        if temp != None:
            # traverse list until element found or end of list
            while temp.next != None:
                if temp.value == find:
                    return True
                else:
                    temp = temp.next

            # check value in last node
            if temp.value == find:

                return True
            else:
                return False

    def print_list(self):
        temp = self.head

        while (temp):
            print(temp.value)
            temp = temp.next

# end of class linked_list


# ==========================

ll = linked_list()
ll.insert_front(5)
ll.insert_front(1)
ll.insert_front(3)

print("Print the linked list")
ll.print_list()

print("Delete Node")
deleted = ll.delete_node(5)
print(deleted)
ll.print_list()


print("Search")
found = ll.search(3)
print (found)