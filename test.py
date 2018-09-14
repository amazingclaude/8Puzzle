import puzzle
import sys
import math
import copy
from heapq import *
heap=[]
item=[1,2,3,4]
heappush(heap,item)
heappush(heap,[5,6,7,8])
print(heap)
print(heap[1][1])


heap.pop(min(heap))
print(heap)



