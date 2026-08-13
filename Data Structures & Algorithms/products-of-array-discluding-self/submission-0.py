class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # productArray = list()
        # # Brute force
        # # O(n^2) time; O(n) space
        # for i in range(len(nums)):
        #     # Find product of all other integer items
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]

        #     # Place product in nums array
        #     productArray[i] = product

        # return productArray

        # O(n) solution

        # Loop through array and calculate total product of all nums in array
        totalProduct = 1
        zerosIndices = set()
        productArray = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                zerosIndices.add(i)
            else:
                totalProduct *= nums[i]

        if len(zerosIndices) == 0:
            for j in range(len(nums)):
                productArray[j] = totalProduct // nums[j]
        elif len(zerosIndices) == 1:
            zeroIdx = zerosIndices.pop()
            for j in range(len(nums)):
                if j == zeroIdx:
                    productArray[j] = totalProduct
                else:
                    productArray[j] = 0
        else:
            for j in range(len(nums)):
                productArray[j] = 0

        return productArray
        