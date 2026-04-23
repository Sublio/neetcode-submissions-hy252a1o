class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        queue = deque(s)
        for s in shift:
            direction, step = s[0], s[1]
            queue.rotate(-step) if direction == 0 else queue.rotate(step)
        return "".join([str(val) for val in queue])

        