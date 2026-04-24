class Logger:

    def __init__(self):
        self.allowed_stamps = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.allowed_stamps: 
            last_stamp = self.allowed_stamps[message]
            if timestamp >= last_stamp:
                self.allowed_stamps[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.allowed_stamps[message] = timestamp + 10
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
