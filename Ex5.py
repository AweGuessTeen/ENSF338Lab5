# Question 1

class queue_array:
    def __init__(this, capacity):
        this.capacity = capacity
        this.queue = [None] * capacity
        this.front = this.rear = -1

    def is_empty(this):
        return this.front == -1

    def is_full(this):
        return (this.rear + 1) % this.capacity == this.front

    def enqueue(this, element):
        if this.is_full():
            print("enqueue None")
        else:
            if this.is_empty():
                this.front = 0
            this.rear = (this.rear + 1) % this.capacity
            this.queue[this.rear] = element
            print(f"enqueue {element}")

    def dequeue(this):
        if this.is_empty():
            print("dequeue None")
        else:
            element = this.queue[this.front]
            this.queue[this.front] = None
            if this.front == this.rear:
                this.front = this.rear = -1
            else:
                this.front = (this.front + 1) % this.capacity
            print(f"dequeue {element}")

    def peek(this):
        if this.is_empty():
            print("peek None")
        else:
            element = this.queue[this.front]
            print(f"peek {element}")


class Node:
    def __init__(this, data):
        this.data = data
        this.next = None
        
# Question 2

class queue_linked_list:
    def __init__(this):
        this.front = this.rear = None

    def is_empty(this):
        return this.front is None

    def enqueue(this, element):
        new_node = Node(element)
        if this.is_empty():
            this.front = this.rear = new_node
            new_node.next = this.front
        else:
            this.rear.next = new_node
            this.rear = new_node
            this.rear.next = this.front
        print(f"enqueue {element}")

    def dequeue(this):
        if this.is_empty():
            print("dequeue None")
        else:
            element = this.front.data
            if this.front == this.rear:
                this.front = this.rear = None
            else:
                this.front = this.front.next
                this.rear.next = this.front
            print(f"dequeue {element}")

    def peek(this):
        if this.is_empty():
            print("peek None")
        else:
            element = this.front.data
            print(f"peek {element}")

# Question 3

operations = [
    "MyQueue.enqueue(1)",
    "MyQueue.enqueue(2)",
    "MyQueue.enqueue(3)",
    "MyQueue.peek()",
    "MyQueue.dequeue()",
    "MyQueue.peek()",
    "MyQueue.dequeue()",
    "MyQueue.dequeue()",
    "MyQueue.dequeue()",
    "MyQueue.peek()",
    "MyQueue.enqueue(4)",
    "MyQueue.enqueue(10)",
    "MyQueue.peek()",
    "MyQueue.dequeue()",
    "MyQueue.peek()",
    "MyQueue.enqueue(11)",
    "MyQueue.enqueue(22)",
    "MyQueue.enqueue(33)",
    "MyQueue.peek()",
    "MyQueue.dequeue()",
    "MyQueue.peek()",
    "MyQueue.dequeue()",
    "MyQueue.dequeue()",
    "MyQueue.dequeue()",
    "MyQueue.peek()",
    "MyQueue.enqueue(14)",
    "MyQueue.enqueue(110)",
    "MyQueue.peek()",
    "MyQueue.dequeue()",
    "MyQueue.peek()",
    "MyQueue.enqueue(1)",
    "MyQueue.enqueue(2)",
    "MyQueue.enqueue(3)",
    "MyQueue.peek()",
    "MyQueue.dequeue()",
    "MyQueue.peek()",
    "MyQueue.dequeue()",
    "MyQueue.dequeue()",
    "MyQueue.dequeue()",
    "MyQueue.peek()",
    "MyQueue.enqueue(4)",
    "MyQueue.enqueue(10)",
]

MyQueue = queue_array(5)
for operation in operations:
    eval(operation)

linked_list_queue = queue_linked_list()
for operation in operations:
    eval(operation)
