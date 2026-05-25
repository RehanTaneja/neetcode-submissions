class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        uniq = set(nums)
        lst_uniq = []
        for i in uniq:
            lst_uniq.append(i)
        lst_uniq = sorted(lst_uniq)
        print(lst_uniq)
        max_consec = 1
        current_consec = 1
        for i in range(len(lst_uniq)-1):
            if lst_uniq[i+1] == lst_uniq[i] + 1:
                current_consec += 1
            else :
                if current_consec+1 > max_consec:
                    max_consec = current_consec 
                    current_consec = 1
                else:
                    current_consec = 1
        if current_consec > max_consec:
            max_consec = current_consec
        return max_consec