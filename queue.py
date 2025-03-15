queue=[]
queue.append("Manu")
queue.append("Radha")
queue.append("Akhil")
queue.append("Ravi")
print("Queue after enqueues:",queue)
front_item=queue.pop(0)
print("Dequeued item:",front_item)
print("Queue after dequeue:",queue)
peek_item = queue[0]
print("front_item(peek):",peek_item)
is_empty = len(queue) == 0
print("Is the queue empty?:",is_empty)
queue_size = len(queue)
print("Queue size:",queue_size)

