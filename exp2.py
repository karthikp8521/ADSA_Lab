# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:

    def __init__(self):
        self.head = None


    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node


    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp


    # Insert at position (1-based index)
    def insert_position(self, pos, data):
        if pos == 1:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(pos - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        new_node.next = temp.next
        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node
        new_node.prev = temp


    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None


    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.prev.next = None


    # Delete by value
    def delete_value(self, key):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev


    # Forward traversal
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


    # Backward traversal
    def display_backward(self):
        temp = self.head
        if temp is None:
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# Driver program
dll = DoublyLinkedList()

dll.insert_beginning(10)
dll.insert_beginning(5)
dll.insert_end(20)
dll.insert_position(3, 15)

print("Forward Traversal:")
dll.display_forward()

print("Backward Traversal:")
dll.display_backward()

dll.delete_beginning()
print("After deleting beginning:")
dll.display_forward()

dll.delete_end()
print("After deleting end:")
dll.display_forward()

dll.delete_value(15)
print("After deleting value 15:")
dll.display_forward()