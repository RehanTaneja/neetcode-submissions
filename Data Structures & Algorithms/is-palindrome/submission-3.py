class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        news = ""
        for i in s:
            if i != " " and i in "1234567890abcdefghijklmnopqrstuvwxyz":
                news += i
        print(news)
        print(news[::-1])
        return news == news[::-1]