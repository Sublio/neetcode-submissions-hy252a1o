class StringIterator:

    def __init__(self, compressedString: str):
        self.orig_string = ""
        self.pointer = -1

        n = 0

        while n < len(compressedString):
            cur_char = compressedString[n]
            n+=1
            num_str = ""
            while n < len(compressedString) and compressedString[n].isdigit():
                num_str += compressedString[n]
                n += 1

            count = int(num_str)
            self.orig_string += cur_char * count
        
    def next(self) -> str:
        self.pointer +=1
        return self.orig_string[self.pointer] if self.pointer < len(self.orig_string) else " "

    def hasNext(self) -> bool:
        return self.pointer < len(self.orig_string)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
