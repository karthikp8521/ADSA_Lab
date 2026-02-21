class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size


    # Push operation
    def push(self, element):
        if len(self.stack) == self.size:
            print("Stack Overflow")
        else:
            self.stack.append(element)
            print(element, "pushed into stack")


    # Pop operation
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            removed = self.stack.pop()
            print(removed, "popped from stack")


    # Peek operation
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element is:", self.stack[-1])


    # Display stack
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements (Top to Bottom):")
            for i in reversed(self.stack):
                print(i)


# Driver Program
size = int(input("Enter stack size: "))
s = Stack(size)

while True:
    print("\n1.Push  2.Pop  3.Peek  4.Display  5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter element: "))
        s.push(val)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")