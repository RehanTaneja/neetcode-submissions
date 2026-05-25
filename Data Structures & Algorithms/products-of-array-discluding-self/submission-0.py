class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            zero_cnt = 0
            for i in nums:
                if i == 0:
                    zero_cnt+=1
            if zero_cnt == 1:
                prods = []
                p = 1
                for i in nums:
                    if i != 0:
                        p*=i
                for i in nums:
                    if i ==0:
                        prods.append(p)
                    else:
                        prods.append(0)
                return prods
            else:
                prods = []
                for i in nums:
                    prods.append(0)
                return prods
        prods = []
        p = 1
        for i in nums:
            p *= i
        for i in nums:
            ans = p//i
            prods.append(ans)
        return prods