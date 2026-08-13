class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        bestContainerArea = 0

        while l < r:
            # evaluate area of container with these bounds
            area = (r - l) * min(heights[l], heights[r])

            if area > bestContainerArea:
                bestContainerArea = area

            if heights[l] < heights[r]:
                nextL = l + 1
                # Increment l until we find next bar with a greater height
                while heights[nextL] <= heights[l]:
                    nextL += 1
                l = nextL
            elif heights[l] == heights[r]:
                # We must simulate moving both sides
                stepSize = 1
                for stepSize in range(1, len(heights)):
                    if l + stepSize >= r - stepSize:
                        # There are no better options
                        return bestContainerArea

                    if heights[l + stepSize] > heights[l] and heights[l + stepSize] > heights[r - stepSize]:
                        l += stepSize
                        break
                    elif heights[r - stepSize] > heights[r] and heights[r - stepSize] > heights[l + stepSize]:
                        r -= stepSize
                        break
                    elif (heights[l + stepSize] > heights[l] and heights[r - stepSize] > heights[r] and 
                        heights[r - stepSize] == heights[l + stepSize]):
                        l += stepSize
                        r -= stepSize
                        break
                
            else:
                nextR = r - 1
                # Decrement r until we find a bar with a greater heightr
                while heights[nextR] <= heights[r]:
                    nextR -= 1
                r = nextR

        return bestContainerArea
        