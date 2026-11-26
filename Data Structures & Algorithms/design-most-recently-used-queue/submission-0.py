class MRUQueue:
    def __init__(self, n: int):
        self.queue = []
        for i in range(1,n+1):
            self.queue.append(i)

    def fetch(self, k: int) -> int:
        elem = self.queue[k-1]
        self.queue.append(self.queue.pop(k-1))
        return elem
