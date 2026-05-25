class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        threeSum = []
        for i in range(0,len(nums)-2):
            sumToFind = 0 - nums[i]
            j,k = i+1,len(nums)-1
            while j<k:
                if nums[j]+nums[k] == sumToFind:
                    threeSum.append([nums[i],nums[j],nums[k]])
                    print(threeSum)
                    j+=1
                elif nums[j]+nums[k] < sumToFind:
                    j+=1
                else:
                    k-=1
        ans = list(list(n) for n in list({tuple(nested) for nested in threeSum}))
        print(ans)
        return ans