class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for d in details:
            age = int(d[-4:-2])
            if age > 60:
                res +=1
        return res
        