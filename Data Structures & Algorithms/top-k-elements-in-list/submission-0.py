class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}

        for i in nums:
            ans[i] = ans.get(i, 0) + 1

        sorted_ans = sorted(ans, key=ans.get, reverse=True)
        return sorted_ans[:k]