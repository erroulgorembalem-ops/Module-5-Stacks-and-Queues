# Module 5 Laboratory Activity: Stacks and Queues
# Implements array and linked-list stacks and queues, plus two application exercises.

class ArrayStack:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Stack capacity must be greater than zero.")
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push onto a full stack.")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack.")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: there is no top element.")
        return self.data[self.top]

    def __str__(self):
        return f"Stack (bottom -> top): {self.data[:self.top + 1]}"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False  # No fixed capacity; limited only by available memory.

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: there is no top element.")
        return self.top.value

    def __str__(self):
        values, current = [], self.top
        while current is not None:
            values.append(current.value)
            current = current.next
        return f"Stack (top -> bottom): {values}"


class ArrayQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Queue capacity must be greater than zero.")
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: cannot enqueue into a full queue.")
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue.")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: there is no front element.")
        return self.data[self.front]

    def __str__(self):
        items = [self.data[(self.front + i) % len(self.data)]
                 for i in range(self.size)]
        return f"Queue (front -> rear): {items}"


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False  # No fixed capacity; limited only by available memory.

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue.")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: there is no front element.")
        return self.front.value

    def __str__(self):
        values, current = [], self.front
        while current is not None:
            values.append(current.value)
            current = current.next
        return f"Queue (front -> rear): {values}"


def choose_structure():
    print("\\nChoose a data structure:")
    print("1. Array Stack")
    print("2. Linked-List Stack")
    print("3. Circular Array Queue")
    print("4. Linked-List Queue")
    choice = input("Enter choice (1-4): ").strip()
    if choice == "1":
        return ArrayStack(int(input("Stack capacity: ")))
    if choice == "2":
        return LinkedStack()
    if choice == "3":
        return ArrayQueue(int(input("Queue capacity: ")))
    if choice == "4":
        return LinkedQueue()
    print("Invalid choice.")
    return None


def run_menu():
    structure = choose_structure()
    if structure is None:
        return

    is_stack = isinstance(structure, (ArrayStack, LinkedStack))
    while True:
        print("\\nCurrent state:", structure)
        if is_stack:
            print("1. Push   2. Pop   3. Peek   4. Is empty?   5. Is full?   6. Change structure   7. Exit")
        else:
            print("1. Enqueue  2. Dequeue  3. Peek front  4. Is empty?  5. Is full?  6. Change structure  7. Exit")
        action = input("Choose an operation: ").strip()
        try:
            if action == "1":
                value = input("Enter value: ")
                if is_stack:
                    structure.push(value)
                else:
                    structure.enqueue(value)
            elif action == "2":
                print("Removed:", structure.pop() if is_stack else structure.dequeue())
            elif action == "3":
                print("Top/front:", structure.peek() if is_stack else structure.peek_front())
            elif action == "4":
                print("Empty:", structure.is_empty())
            elif action == "5":
                print("Full:", structure.is_full())
            elif action == "6":
                structure = choose_structure()
                if structure is None:
                    print("Keeping the previous structure.")
                    return
                is_stack = isinstance(structure, (ArrayStack, LinkedStack))
            elif action == "7":
                print("Program ended.")
                break
            else:
                print("Invalid operation. Please choose a listed number.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
        print("State after operation:", structure)


def check_balanced_parentheses(expression):
    matching = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != matching[char]:
                return False
    return len(stack) == 0


def print_queue_exercise():
    jobs = ArrayQueue(10)
    print("\\nPrint Queue Exercise")
    print("Enter up to 10 print jobs. Leave the Job ID blank to stop.")
    while not jobs.is_full():
        job_id = input("Job ID: ").strip()
        if not job_id:
            break
        try:
            pages = int(input("Number of pages: "))
            if pages <= 0:
                print("Page count must be positive.")
                continue
        except ValueError:
            print("Please enter a whole number for pages.")
            continue
        jobs.enqueue({"id": job_id, "pages": pages})
        print("Queue state:", jobs)

    print("\\nPrinting jobs in FIFO order:")
    position = 1
    while not jobs.is_empty():
        job = jobs.dequeue()
        print(f"Wait position {position}: Job {job['id']} ({job['pages']} pages)")
        position += 1


def application_exercises():
    expression = input("Enter an expression containing parentheses/brackets/braces: ")
    if check_balanced_parentheses(expression):
        print("The parentheses/brackets/braces are balanced.")
    else:
        print("The parentheses/brackets/braces are NOT balanced.")
    print_queue_exercise()


if __name__ == "__main__":
    print("MODULE 5 LABORATORY: STACKS AND QUEUES")
    while True:
        print("\\nMain menu")
        print("1. Run stack/queue menu")
        print("2. Run application exercises")
        print("3. Test underflow and overflow")
        print("4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            run_menu()
        elif choice == "2":
            application_exercises()
        elif choice == "3":
            print("\\nTesting ArrayStack errors:")
            stack = ArrayStack(1)
            try:
                stack.pop()
            except IndexError as error:
                print(error)
            stack.push("A")
            try:
                stack.push("B")
            except OverflowError as error:
                print(error)

            print("\\nTesting ArrayQueue errors:")
            queue = ArrayQueue(1)
            try:
                queue.dequeue()
            except IndexError as error:
                print(error)
            queue.enqueue("Job-A")
            try:
                queue.enqueue("Job-B")
            except OverflowError as error:
                print(error)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")
