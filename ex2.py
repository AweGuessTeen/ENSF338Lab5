# Imports
import random
import timeit

# Classes and Definitions
# First priority queue implementation
class MergePriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        self.queue = self._merge_sort(self.queue)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        # else:
            # print("Merge Queue is empty")
        # Should be included but is excluded to save time
            

    def is_empty(self):
        return len(self.queue) == 0

    def _merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self._merge_sort(left_half)
            self._merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        return arr

# Second priority queue implementation
class InsertPriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        if not self.queue or item >= self.queue[-1]:
            self.queue.append(item)
        else:
            for i in range(len(self.queue)):
                if item < self.queue[i]:
                    self.queue.insert(i, item)
                    break

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        # else:
            # print("Insert Queue is empty")
        # Should be included but is excluded to save time

    def is_empty(self):
        return len(self.queue) == 0
    
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

# Main Code
merge_total = 0
for _ in range(100):
    merge_queue = MergePriorityQueue()
    tasks = rand_tasks(1000)
    merge_total += time_task(merge_queue, tasks)

insert_total = 0
for _ in range(100):
    insert_queue = InsertPriorityQueue()
    tasks = rand_tasks(1000)
    insert_total += time_task(insert_queue, tasks)

merge_average = merge_total / 100
insert_average = insert_total / 100
print("Average time for MergePriorityQueue:", merge_average)
print("Average time for InsertPriorityQueue:", insert_average)

'''
Question 5: Discuss the results: which implementation is faster? Why?
Based on the average times, the second priority queue imlementation, which is sorted upon insertion,
is faster by a factor of 100. One big factor which may explain the huge difference in times
is how the first priority queue class requires a merge sort after every task.
This wastes a lot of time, especially when the queue is already properly sorted.
When looking at each operation, enqueue has a complexity of O(n log n) for MergePriorityQueue
and a complexity of O(n) for InsertPriorityQueue. Meanwhile, dequeue has a commplexity of
O(1) since it just pops the first element. Based of this analysis, the InsertPriorityQueue
should complete tasks faster as functions with a complexity of O(n) will generally be faster
than those with a complexity of O(n log n). This can also be attributed to the idea that
enqueue tasks are more more likely to generate than dequeue tasks.
'''