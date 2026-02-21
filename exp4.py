class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size


    # Enqueue operation
    def enqueue(self, element):
        if len(self.queue) == self.size:
            print("Queue Overflow")
        else:
            self.queue.append(element)
            print(element, "inserted into queue")


    # Dequeue operation
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow")
        else:
            removed = self.queue.pop(0)
            print(removed, "removed from queue")


    # Peek operation
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element is:", self.queue[0])


    # Display queue
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue elements (Front to Rear):")
            for i in self.queue:
                print(i)


# Driver Program
size = int(input("Enter queue size: "))
q = Queue(size)

while True:
    print("\n1.Enqueue  2.Dequeue  3.Peek  4.Display  5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter element: "))
        q.enqueue(val)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.peek()

    elif choice == 4:
        q.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")