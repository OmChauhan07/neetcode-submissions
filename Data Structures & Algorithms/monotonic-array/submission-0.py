class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        up = 0
        for i in range(0, len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                up += 1
            else:
                break
        down = 0
        for i in range(0, len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                down += 1
            else:
                break

        if up == len(nums) - 1 or down == len(nums) - 1:
            return True
        else:
            return False