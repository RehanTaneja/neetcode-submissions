class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ans = 0
        max_yet = -100000
        for i in nums:
            if ans < 0:
                ans = max(ans,ans+i,i)
            else:
                ans += i
            max_yet = max(ans,max_yet)
        return max_yet
        