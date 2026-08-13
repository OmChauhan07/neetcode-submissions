class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        if i not in nums:
            return i

        while i <= max(nums):
            if i not in nums:
                break
            i += 1

        return i