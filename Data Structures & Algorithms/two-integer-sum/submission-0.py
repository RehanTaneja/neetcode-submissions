class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==2:
            return [0,1]
        #nums_sorted = sorted(nums)
        j = len(nums)-1
        while j>0:
            i=0
            while i<j:
                if nums[i]+nums[j]==target:
                    return [i,j]
                i+=1
            j-=1