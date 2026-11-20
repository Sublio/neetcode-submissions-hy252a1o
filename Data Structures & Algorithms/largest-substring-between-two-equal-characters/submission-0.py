class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_seen = 0
        cnt_s = Counter(s)
        more_than_one_chars =[]
        for k,v in cnt_s.items():
            if v >1:
                more_than_one_chars.append(k)
        for c in more_than_one_chars:
            indices = [i for i, char in enumerate(s) if char == c]
            max_distance = max(indices) - min(indices)
            max_seen = max(max_seen, max_distance)
        return max_seen-1
        