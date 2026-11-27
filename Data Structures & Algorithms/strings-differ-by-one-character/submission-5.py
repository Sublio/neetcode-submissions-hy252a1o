class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        if not dict:
            return False
        m = len(dict[0])
        for i in range(m):
            seen = set()
            for word in dict:
                pattern = word[:i] + word[i+1:]
                if pattern in seen:
                    return True
                seen.add(pattern)
        return False