class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = set()
        left = 0
        longest = 0
        right = 0
        while right < len(s):
            while s[right] in uniq:
                uniq.remove(s[left])
                left+=1
            longest = max(longest,right-left+1)
            uniq.add(s[right])
            right+=1
        return longest
        
        