class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in range(len(nums1)):
            index_num2 = nums2.index(nums1[i])
            found = -1
            for j in range(index_num2 + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    found = nums2[j]
                    break
            res.append(found)
        return res