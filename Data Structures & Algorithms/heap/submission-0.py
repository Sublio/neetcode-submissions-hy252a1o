class MinHeap:

    def __init__(self):
        self.heap = []

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] > self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break

    def pop(self) -> int:
        if not self.heap:
            return -1
        if len(self.heap) == 1:
            return self.heap.pop()
        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        i = 0
        n = len(self.heap)
        while True:
            left, right, smallest = 2 * i + 1, 2 * i + 2, i
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
        return top

    def top(self) -> int:
        return self.heap[0] if self.heap else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = nums
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            j = i
            while True:
                left, right, smallest = 2 * j + 1, 2 * j + 2, j
                if left < n and self.heap[left] < self.heap[smallest]:
                    smallest = left
                if right < n and self.heap[right] < self.heap[smallest]:
                    smallest = right
                if smallest == j:
                    break
                self.heap[j], self.heap[smallest] = self.heap[smallest], self.heap[j]
                j = smallest