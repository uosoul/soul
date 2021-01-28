from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        bigger = deque()
        for i, n in enumerate(nums):
            # make sure the rightmost one is the smallest
            while bigger and nums[bigger[-1]] <= n:
                bigger.pop()

            # add in
            bigger += [i]

            # make sure the leftmost one is in-bound
            if i - bigger[0] >= k:
                bigger.popleft()

            # if i + 1 < k, then we are initializing the bigger array
            if i + 1 >= k:
                res.append(nums[bigger[0]])
        return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d +=i,
            if d[0] == i-k:
                d.popleft()
            if i>=k-1:
                out += nums[d[0]],
        return out










#双端队列的实现
class Queue(object):
        def __init__(self):
                self.__List[]
                
        def enqueue(self,item):
                self.__list.append(item)

        def dequeue(self):
                return self.pop(0)

        def is_empty(self):
                return self.__list ==[]

        def size(self):
                return len(self.__list)







        








