class Node:
    def __init__(self, value):
        self.value  = value
        self.next   = None

class LinkedList:
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print (temp.value)
            temp = temp.next

    # Add a new node to the end of the linked list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next  = new_node
            self.tail       = new_node
        self.length += 1
        return True

    # Remove and return the value of the node at the end of the linked list
    def pop(self):
        if self.length == 0:
            return None
        else:
            temp_node   = self.head
            pre_node    = self.head
            while(temp_node.next):
                pre_node    = temp_node
                temp_node   = temp_node.next
            self.tail       = pre_node
            self.tail.next  = None
            self.length     -= 1
            if self.length  == 0:
                self.head   = None
                self.tail   = None
            return temp_node.value

    # Add a new node to the beginning of the linked list
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next   = self.head
            self.head       = new_node
        self.length += 1
        return True
    
    # Remove and return the value of the first Node 
    # at the beginning of the linked list
    def popFirst(self):
        if self.length == 0:
            return None
        else:
            temp_Node       = self.head
            self.head       = self.head.next
            temp_Node.next  = None
        self.length -= 1
        if(self.length == 0):
            self.tail = None
        return temp_Node.value
    
    # Return value of the node by index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp_Node = self.head
            return temp_Node.value
            
    # def insert(self ,index ,value):

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.prepend(1)
print(my_linked_list.popFirst())
print(my_linked_list.popFirst())
print(my_linked_list.popFirst())
print(my_linked_list.popFirst())
