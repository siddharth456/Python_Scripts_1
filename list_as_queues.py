'''Lists can also be implemented as queues,where the first element added is the first element retrieved
 However lists are not efficient in this case.While append and pop from the end of the list is fast
 inserts or pops at the beginning of the list is slow'''

'''To implement a queue,use collections.deque which is designed for faster appends and pops from both ends'''

from collections import deque
testqueue = deque(['Eric','Shane','King'])
testqueue.append('Terry')
testqueue.append('Healy')
print("Testqueue after appends:",testqueue)
testqueue.popleft()
testqueue.popleft()
testqueue.pop()
print(testqueue)
