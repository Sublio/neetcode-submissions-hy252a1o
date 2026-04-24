class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.vals  = []
        

    def next(self, val: int) -> float:
        self.vals.append(val)
        if self.size >= len(self.vals):
            return float(sum(self.vals)/len(self.vals))
        else:
            return float(sum(self.vals[-self.size:])/self.size)