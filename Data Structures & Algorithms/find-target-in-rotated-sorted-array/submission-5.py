class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0
        if target > nums[0]:
            # target is between index 0 to peak
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = (l + r) // 2

                if nums[m] == target:
                    return m
                elif nums[m] < nums[0] or nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
                
            # target is not in nums
            return -1
        else:
            # target is between trough and len(nums) - 1
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = (l + r) // 2

                if nums[m] == target:
                    return m
                elif nums[m] >= nums[0] or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            # target is not in nums
            return -1            


        