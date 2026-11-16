class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [index, height]
        maxArea = 0
        for idx, height in enumerate(heights):
            start = idx
            while stack and height < stack[-1][1]:
                i,h = stack.pop()        
                maxArea = max(maxArea, h*(idx-i))
                start = i
            stack.append([start, height])

        while stack:
            idx , height = stack.pop()
            maxArea = max(maxArea, (len(heights)-idx)*height)

        return maxArea