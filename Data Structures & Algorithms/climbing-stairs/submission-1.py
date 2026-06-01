class Solution:
    def climbStairs(self, n: int) -> int:
        opt = [0,1,2]
        for i in range(3,n+1):
            opt.append(opt[i-1] + opt[i-2])
        return opt[n]
        