from typing import List
from collections import OrderedDict, deque

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.count = {}
        self.unique_queue = deque()
        self.in_queue = set()
        
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.unique_queue and self.count[self.unique_queue[0]] > 1:
            self.unique_queue.popleft()
        
        if self.unique_queue:
            return self.unique_queue[0]
        return -1

    def add(self, value: int) -> None:
        if value in self.count:
            self.count[value] += 1

            if value in self.in_queue:
                self.in_queue.remove(value)
        else:
            self.count[value] = 1
            if value not in self.in_queue:
                self.unique_queue.append(value)
                self.in_queue.add(value)