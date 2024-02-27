# Imports
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Classes and Definitions
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if not self.is_empty():
            removed_data = self.tail.data

            if self.head == self.tail:
                self.head = self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next

                current.next = None
                self.tail = current

            return removed_data

    def is_empty(self):
        return self.head is None
    
def rand_tasks(num_tasks):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < 0.7:
            task = ('enqueue', random.randint(1, 100))
        else:
            task = ('dequeue',)
        tasks.append(task)
    return tasks

def time_task(priority_queue, tasks):
    def run_tasks():
        for task in tasks:
            if task[0] == 'enqueue':
                priority_queue.enqueue(task[1])
            elif task[0] == 'dequeue':
                priority_queue.dequeue()

    return timeit.timeit(run_tasks, number=1)

# Main code
num_tasks = 10000
array_times = []
list_times = []

for _ in range(100):
    tasks = rand_tasks(num_tasks)

    array_queue = ArrayQueue()
    array_time = time_task(array_queue, tasks)
    array_times.append(array_time)

    list_queue = LinkedListQueue()
    list_time = time_task(list_queue, tasks)
    list_times.append(list_time)

# Plot the distribution of times
# Assure consistent ranges
data_range = max(max(array_times), max(list_times)) - min(min(array_times), min(list_times))
bins = np.linspace(min(min(array_times), min(list_times)), max(max(array_times), max(list_times)), 20)

plt.hist(array_times, alpha=0.5, bins=bins, label='ArrayQueue')
plt.hist(list_times, alpha=0.5, bins=bins, label='LinkedListQueue')
plt.legend(loc='upper right')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Times for ArrayQueue and LinkedListQueue')
plt.show()

'''
Question 5: Discuss the results
After running the program many times, it is clear there is a considerable gap between these
two implementations of queues. More specifically, the ArrayQueue class peforms tasks
much faster than the LinkedListClass. This can be attributed to how the latter is implemented.
It is usually recommended for linked list queues to enqueue at the tail and dequeue at the head.
This would result in a complexity of O(1) for each of those tasks. In this case,
we enqueue at the head and dequeue at the tail. The first always has a complexity of O(1),
but the dequeue operation is now O(n) as it must traverse through the list to find the node
before the tail. On the other hand, the array queue implements enqueue and dequeue operations
with a complexity of O(1) as it simply inserts at the end and pops the first element.
'''