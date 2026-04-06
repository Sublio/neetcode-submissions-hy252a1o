class LinkedList:
    
    def __init__(self):
        self.list = []
        

    
    def get(self, index: int) -> int:
        if 0 <= index < len(self.list):
            return self.list[index]
        else:
            return -1

    def insertHead(self, val: int) -> None:
        self.list.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.list.append(val)
        

    def remove(self, index: int) -> bool:
        if 0 <= index < len(self.list):
            self.list.pop(index)
            return True
        else:
            return False
        

    def getValues(self) -> List[int]:
        return self.list
        
