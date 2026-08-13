class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = (r + l) // 2
            
            if nums[m] > nums[n - 1]:
                l = m + 1
            else:
                r = m

        return nums[l]


