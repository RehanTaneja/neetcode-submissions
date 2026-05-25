def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    letters_s={}
    letters_t={}
    for i in range(len(s)):
        if s[i] not in letters_s.keys():
            letters_s[s[i]] = 1
        else:
            letters_s[s[i]] += 1
    for i in range(len(t)):
        if t[i] not in letters_s.keys():
            return False
        if t[i] not in letters_t.keys():
            letters_t[t[i]] = 1
        else:
            letters_t[t[i]] += 1
    for i in range(len(t)):
        if letters_s[t[i]] != letters_t[t[i]]:
            return False
    return True

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagrams_lst = []
        if len(strs)<=1:
            return [strs]
        j = len(strs)-1
        added=[]
        while j>=0:
            i = 0
            anagrams = [strs[j]]
            while i<j:
                if isAnagram(strs[i],strs[j]):
                    anagrams.append(strs[i])
                i+=1
            j-=1
            status = False
            for i in anagrams:
                if i in added:
                    status = True
            if not status:
                groupAnagrams_lst.append(anagrams[::-1])
                for i in anagrams:
                    added.append(i)
        return groupAnagrams_lst[::-1]





