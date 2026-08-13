class Solution:
    def hasDuplicate(self, nums : List) -> bool:
        nums_as_set = set(nums)

        if (len(nums_as_set) != len(nums)):
            return True
        
        return False
         