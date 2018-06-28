# y=5/2
# print("%.3f" % y)

import queue

# taking an object of Queue()
q = queue.Queue()

# enqueueing some value in the object of Queue
q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E')

# retrieving the values of the Queue
for i in range(q.qsize()):
   print(q.get())

#o/p A B C D E