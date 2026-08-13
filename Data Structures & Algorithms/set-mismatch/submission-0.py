class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        # duplicate
        count = Counter(nums)
        for i, val in count.items():
            if val == 2:
                dup = i

        # missing
        j = 1
        while j < len(nums):
            if j not in nums:
                break
            j += 1
            # miss = j


        return [dup, j]