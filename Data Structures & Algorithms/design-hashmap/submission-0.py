class MyHashMap:

    def __init__(self):
        self.map = {}
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
        else:
            self.map[key] = value
        

    def get(self, key: int) -> int:
        return self.map[key] if key in self.map else -1
        

    def remove(self, key: int) -> None:
        self.map.pop(key, None)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)