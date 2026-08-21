class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1 #declare the pointers

        leftMax, rightMax = heights[left], heights[right] # intialize the maxes
        result = 0
        while left < right: # ensure the pointer do not pass each other
            area = (min(leftMax, rightMax)) * (right - left) # height * width
            if heights[left] > heights[right]: # if the left pointer index value is bigger
                right -= 1 # move right left cause its the limiting wall
                if rightMax < heights[right]:
                    rightMax = heights[right]
            else:
                left += 1 # move left right cause its the limitiing wall
                if leftMax < heights[left]:
                    leftMax = heights[left]
            if result < area:
                result = area
        return result
