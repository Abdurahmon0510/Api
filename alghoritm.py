def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [10, 23, 45, 70, 11, 15]
target = 70
result = linear_search(arr, target)
print(f"Element {target} found at index {result}" if result != -1 else "Element not found")


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [10, 23, 45, 70, 80, 100]
target = 70
result = binary_search(arr, target)
print(f"Element {target} found at index {result}" if result != -1 else "Element not found")


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return None


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(f"Stack Top: {stack.top()}")
print(f"Popped: {stack.pop()}")
print(f"Stack Top After Pop: {stack.top()}")

from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(f"Queue Front: {queue.front()}")
print(f"Dequeued: {queue.dequeue()}")
print(f"Queue Front After Dequeue: {queue.front()}")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.print_list()
