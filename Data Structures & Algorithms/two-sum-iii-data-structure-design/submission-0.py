class TwoSum:
    def __init__(self):
        self.store= []
    def add(self, number: int) -> None:
        self.store.append(number)
    def find(self, value: int) -> bool:
        seen = {}
        for i in range(len(self.store)):
            cur_num = self.store[i]
            cur_diff = value - cur_num
            if cur_diff not in seen:
                seen[cur_num] = i
            else:
                return True
        return False
