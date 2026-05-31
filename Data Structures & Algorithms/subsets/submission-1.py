class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        if len(nums) == 1:
            return [[],[nums[0]]]
        ss = self.subsets(nums[1:])
        temp = ss.copy()
        for e in temp:
            t = e + [nums[0]]
            ss += [t]
        return ss
