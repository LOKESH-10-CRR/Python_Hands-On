class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_water = -1
        while left < right:
            width = right-left
            max_water = max(min(height[left], height[right])*width, max_water)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_water
        
        