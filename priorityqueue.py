import queue

q = queue.PriorityQueue()

q.put((1, 'A'))
q.put((3, 'B'))
q.put((2, 'C'))

for i in range(q.qsize()):
    print(q.get())

#o/p (1,'A') (2,'C') (3,'B')