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

        # # O(n) solution

        # # Loop through array and calculate total product of all nums in array
        # totalProduct = 1
        # zerosIndices = set()
        # productArray = [0] * len(nums)
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         zerosIndices.add(i)
        #     else:
        #         totalProduct *= nums[i]

        # if len(zerosIndices) == 0:
        #     for j in range(len(nums)):
        #         productArray[j] = totalProduct // nums[j]
        # elif len(zerosIndices) == 1:
        #     zeroIdx = zerosIndices.pop()
        #     for j in range(len(nums)):
        #         if j == zeroIdx:
        #             productArray[j] = totalProduct
        #         else:
        #             productArray[j] = 0
        # else:
        #     for j in range(len(nums)):
        #         productArray[j] = 0

        # return productArray

        # O(n) solution w/o division
        prefixProduct = [0] * len(nums)
        postfixProduct = [0] * len(nums)
        productArray = [0] * len(nums)

        # Calculate prefix products
        # zeroIdx = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                productOtherThanZero = 1
                for j in range(len(nums)):
                    if j != i:
                        productOtherThanZero *= nums[j]
                productArray[i] = productOtherThanZero
                return productArray
            
            if i == 0:
                prefixProduct[i] = 1
            elif i == 1:
                prefixProduct[i] = nums[0]
            else:
                prefixProduct[i] = prefixProduct[i - 1] * nums[i - 1]
         
        # if zeroIdx >= 0:
        #     productArray[zeroIdx] = prefixProduct[-1] * nums[-1]
        #     return productArray

        # Build postfix array
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                postfixProduct[j] = 1
            elif j == len(nums) - 2:
                postfixProduct[j] = nums[-1]
            else:
                postfixProduct[j] = postfixProduct[j + 1] * nums[j + 1]

        # Use prefix and postfix sum to find product at each index
        for k in range(len(nums)):
            productArray[k] = prefixProduct[k] * postfixProduct[k]

        return productArray
        