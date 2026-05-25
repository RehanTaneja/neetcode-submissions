class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniq = {}
        for i in nums:
            if i in uniq.keys():
                uniq[i] += 1
            else:
                uniq[i] = 1
        uniq = dict(sorted(uniq.items(), key=lambda x:x[1],reverse=True))
        elements = list(uniq.items())
        final = []
        for i in range(k):
            final.append(elements[i][0])
        return final