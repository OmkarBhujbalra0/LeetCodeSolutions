class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l = []
        s = []
        for i in range(0,len(nums)):
            nums[i] = str(nums[i])
        for i in range(0,len(nums)):
            if len(nums[i])%2==0:
                s.append(nums[i])
        return len(s)