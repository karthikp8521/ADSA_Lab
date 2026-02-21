# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class SinglyLinkedList:

    def __init__(self):
        self.head = None


    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
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


    # Insert at position
    def insert_position(self, pos, data):
        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(pos - 2):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next


    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None


    # Delete by value
    def delete_value(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next


    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Driver program
sll = SinglyLinkedList()

sll.insert_beginning(10)
sll.insert_beginning(5)
sll.insert_end(20)
sll.insert_position(3, 15)

print("Linked List:")
sll.display()

sll.delete_beginning()
print("After deleting beginning:")
sll.display()

sll.delete_end()
print("After deleting end:")
sll.display()

sll.delete_value(15)
print("After deleting value 15:")
sll.display()