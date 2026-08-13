class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        start = dict()
        end = dict()
        lenLongestCS = 0
        

        for num in nums:
            # If we've already seen num, it will be in one of the dicts
            if num in start or num in end:
                continue

            # # Mark as seen
            # end[num] = 0

            # We can join two existing CS's with num
            if num - 1 in end and num + 1 in start:                
                newLen = end[num - 1] + 1 + start[num + 1]

                newStartNum = num - end[num - 1]
                newEndNum = num + start[num + 1]

                # Update values
                start[newStartNum] = newLen
                end[newEndNum] = newLen

                if newLen > lenLongestCS:
                    lenLongestCS = newLen

                # Removing interior enpoints
                # end[num - 1] = 0
                # start[num + 1] = 0
                end.pop(num - 1)
                start.pop(num + 1)
            elif num - 1 in end:
                startNum = num - end[num - 1]
                oldLen = start[startNum]

                # end[num - 1] = 0
                end.pop(num - 1)
                end[num] = oldLen + 1
                start[startNum] = start[startNum] + 1

                if oldLen + 1 > lenLongestCS:
                    lenLongestCS = oldLen + 1
            elif num + 1 in start:
                endNum = num + start[num + 1]
                oldLen = start[num + 1]

                # start[num + 1] = 0
                start.pop(num + 1)
                start[num] = oldLen + 1
                
                end[endNum] = end[endNum] + 1

                if oldLen + 1 > lenLongestCS:
                    lenLongestCS = oldLen + 1
            else:
                start[num] = 1
                end[num] = 1
                
                if lenLongestCS < 1:
                    lenLongestCS = 1
        
        return lenLongestCS



            

        # for num in nums:
        #     if num - 1 in SubseqToLength:
        #         # We can add num to an existing consecutive subsequence
        #         length = SubseqToLength[num - 1]

        #         if length + 1 > SubseqToLength.get(num, 0):
        #             # Add to existing subsequence
        #             SubseqToLength.pop(num - 1)
        #             SubseqToLength[num] = length + 1

        #             if length + 1 > largestSubseqLen:
        #                 largestSubseqLen = length + 1
        #     elif num not in SubseqToLength:
        #         SubseqToLength[num] = 1

        #         if 1 > largestSubseqLen:
        #             largestSubseqLen = 1
        
        # return largestSubseqLen


        