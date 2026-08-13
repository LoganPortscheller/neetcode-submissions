class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a set of all numbers that occur in nums
        numsSet = set(nums)
        # sorted list so sortedNums[i] < sortedNums[j] <   
        # sortedNums[k] for every i < j < k    
        sortedNums = sorted(nums)

        # Running set of triplet sets that sum to zero
        triplets = list()

        for i in range(0, len(sortedNums) - 2):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue
            for j in range(i + 1, len(sortedNums) - 1):
                if j > (i + 1) and sortedNums[j] == sortedNums[j - 1]:
                    continue
                # i < j and we are looking for a k where i < j < k and 
                # sortedNums[i] + sortedNums[j] + sortedNums[k] == 0
                thirdNumNeeded = -(sortedNums[i] + sortedNums[j])

                if ((thirdNumNeeded in numsSet and thirdNumNeeded > sortedNums[j]) or 
                    (thirdNumNeeded in numsSet and
                    thirdNumNeeded == sortedNums[j] and
                    sortedNums[j] == sortedNums[j + 1])):
                        triplets.append([sortedNums[i], sortedNums[j], thirdNumNeeded])

        return triplets





        