class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}

        for i, idx in enumerate(nums):
            col = target - idx

            if col in sol:
                return [sol[col],i ]

            sol[idx] = i