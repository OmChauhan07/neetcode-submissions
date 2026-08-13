class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = {}

        for i in nums:
            if i in ans:
                ans[i] = ans.get(i, 0) + 1
            else:
                ans[i] = 1

        res = max(ans, key=ans.get)

        return res
                