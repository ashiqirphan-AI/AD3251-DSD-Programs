class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Example usage

my_queue = Queue()

# Enqueue elements into the queue
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

# Check the size of the queue
print("Queue size:", my_queue.size())  # Output: 3

# Dequeue elements from the queue
print("Dequeued item:", my_queue.dequeue())  # Output: 10
print("Dequeued item:", my_queue.dequeue())  # Output: 20

# Check the size of the queue after dequeuing
print("Queue size:", my_queue.size())  # Output: 1
