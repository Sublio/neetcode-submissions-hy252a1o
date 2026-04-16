class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = []

        for i in range(len(nums1)):
            cur_num = nums1[i]
            mapping.append(nums2.index(cur_num))

        return mapping
        