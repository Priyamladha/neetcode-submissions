class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = height[0],height[-1]
        l,r = 0, len(height)-1
        count = 0
        while l<r:
            if left_max < right_max:
                l +=1
                left_max = max(left_max, height[l])
                count += left_max - height[l]
            else:
                r -=1
                right_max = max(right_max, height[r])
                count += right_max - height[r]

        return count