from typing import List
from collections import deque

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = deque()
        if v1:
            self.queue.append((v1, 0))
        if v2:
            self.queue.append((v2, 0))
    
    def next(self) -> int:
        vec, idx = self.queue.popleft()
        val = vec[idx]
        idx += 1
        if idx < len(vec):
            self.queue.append((vec, idx))
        return val
    
    def hasNext(self) -> bool:
        return len(self.queue) > 0
