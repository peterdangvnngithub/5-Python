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

        if self.length == 0:
            self.tail = None
        
        return temp_Node.value
    
    # Return value of the node by index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp_Node = self.head
            for _ in range(index):
                temp_Node = temp_Node.next
            return temp_Node

    # Set value of the node by index
    def set_value(self, index, value):
        temp_Node = self.get(index)
        if temp_Node:
            temp_Node.value = value
            return True
        return False

    # Insert a node to the linked list by index
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_Node        = Node(value)
        temp_Node       = self.get(index - 1)
        new_Node.next   = temp_Node.next
        temp_Node       = new_Node
        self.length     += 1
        
        return True

    # Remove a node in the linked list by index
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        prev_Node       = self.get(index - 1)
        temp_Node       = prev_Node.next
        prev_Node.next  = temp_Node.next
        temp_Node.next  = None
        self.length     -= 1
        return temp_Node

    # Reverse the linked list
    def reverse(self):
        temp_Node   = self.head
        self.head   = self.tail
        self.tail   = temp_Node
        after_Node  = temp_Node.next
        before_Node = None
        for _ in range(self.length):
            after_Node      = temp_Node.next
            temp_Node.next  = before_Node
            before_Node     = temp_Node
            temp_Node       = after_Node

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.prepend(1)

my_linked_list.insert(3,4)
my_linked_list.print_list()

my_linked_list.reverse()
my_linked_list.print_list()
