class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if target == nums[i] or (target not in nums and target < nums[i]):
                return i
            elif target not in nums and target > nums[len(nums)-1]:
                return len(nums) + i

