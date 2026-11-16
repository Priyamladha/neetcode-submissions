class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxElement = max(heights)
        maxArea = 0
        for i in range(1, maxElement+1):
            width = 0
            for height in heights:
                if height >= i:
                    width +=1
                    # print(height, width, i)
                    maxArea = max(maxArea, width*i)
                else:
                    width = 0
        return maxArea
