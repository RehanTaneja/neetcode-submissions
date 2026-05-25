class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = set()
        longest = 0
        curr = 0
        i = 0
        d = dict()
        while i < len(s):
            uniq.add(s[i])
            curr += 1
            if curr!=len(uniq):
                if curr > longest:
                    longest = len(uniq)
                curr = 0
                uniq.clear()
                i = d[s[i]]
            else:
                d[s[i]] = i
            i+=1
        if curr > longest:
            longest = len(uniq)
        return longest