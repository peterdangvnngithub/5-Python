# Define a Node in LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define LinkedList


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    # Insert after node
    def insertAfter(self, prev_node, new_data):
        # 1. check if the given prev_node exists
        if self.head is None:
            self.head = Node(new_data)
            return

    # Appends a new node at the end

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next


if __name__ == '__main__':
    lList = LinkedList()

    lList.append(1)

    lList.append(3)

    lList.push(0)

    lList.insertAfter(1, 2)

    lList.printLinkedList()
