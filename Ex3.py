# Question 1

class stack_array:
    def __init__(this):
        this.items = []

    def push(this, item):
        this.items.append(item)

    def pop(this):
        if not this.is_empty():
            return this.items.pop()

    def is_empty(this):
        return len(this.items) == 0

# Question 2

class Node:
    def __init__(this, data=None):
        this.data = data
        this.next = None

class stack_linkedlist:
    def __init__(this):
        this.head = None

    def push(this, item):
        new_node = Node(item)
        new_node.next = this.head
        this.head = new_node

    def pop(this):
        if not this.is_empty():
            popped_item = this.head.data
            this.head = this.head.next
            return popped_item

    def is_empty(this):
        return this.head is None

# Question 3

import random

def random_tasks():
    tasks = []
    for i in range(10000):
        task = "push" if random.random() < 0.7 else "pop"
        tasks.append(task)
    return tasks

# Question 4

import timeit

def measure_performance(stack, tasks):
    s = stack()
    for task in tasks:
        if task == "push":
            s.push(1)  
        elif task == "pop":
            s.pop()

tasks = random_tasks()
print("Stack Array takes", timeit.timeit(lambda: measure_performance(stack_array, tasks), number=100), "seconds")
print("Stack Linked List takes", timeit.timeit(lambda: measure_performance(stack_linkedlist, tasks), number=100), "seconds")

# Question 5

import matplotlib.pyplot as plt

def plot_distribution(array_times, linked_list_times):
    plt.hist(array_times, alpha=0.5, label='ArrayStack')
    plt.hist(linked_list_times, alpha=0.5, label='LinkedListStack')
    plt.legend(loc='upper right')
    plt.title('Distribution of Stack Implementation Times')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.show()

# Example usage
array_times = [timeit.timeit(lambda: measure_performance(stack_array, tasks), number=1) for _ in range(100)]
linked_list_times = [timeit.timeit(lambda: measure_performance(stack_linkedlist, tasks), number=1) for _ in range(100)]

plot_distribution(array_times, linked_list_times)



