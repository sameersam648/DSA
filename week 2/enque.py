from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(f"Queue after enqueing : {queue}")

#removing the elements form the queue

front=queue.popleft()
print(f"Dequed element: {front}")
print(f" remaining Queue: {queue}")

front=queue.popleft()
print(f"Dequed element: {front}")
print(f" remaining Queue: {queue}")


#it was intresting and fun to learn about the queue and deque
#deque = double ended queue, it can be used to remove or append elements from both left and right 