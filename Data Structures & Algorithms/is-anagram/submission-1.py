class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        letters_s = {}
        letters_t = {}
        for _,value in enumerate(s):
            if value not in letters_s.keys():
                letters_s[value]=0
            else:
                letters_s[value]+=1
        for i in range(len(t)):
            if t[i] not in letters_s.keys():
                return False
            if t[i] not in letters_t.keys():
                letters_t[t[i]]=0
            else:
                letters_t[t[i]]+=1
        for i in range(len(t)):
            if letters_s[t[i]]!=letters_t[t[i]]:
                return False           
        return True