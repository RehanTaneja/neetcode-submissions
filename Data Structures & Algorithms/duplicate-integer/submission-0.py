class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sort = sorted(nums)
        for i in range(1,len(nums)):
            if nums_sort[i] == nums_sort[i-1]:
                return True
        return False