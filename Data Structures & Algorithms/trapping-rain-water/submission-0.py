class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1 #standard declaration for 2 pointers
        leftMax, rightMax = height[left], height[right] #inital declaration of maxes for both heights, since we start at the edges that would be the starting index.
        res = 0
        while left < right: # ensures that the pointers never pass each other
            if leftMax < rightMax: # if the left pointer index is smaller its the limiting wall
                left += 1 # advance the pointer
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left] #calculate the amount of water able to be stored in the index
            else: # the right pointer index is smaller and is the limiting value for the calculation
                right -= 1
                rightMax = max(rightMax, height[right]) #if the new index of right is bigger than the current rightMax set that new rightMax. In these cases we just always override since it will elimnate a if statement.
                res += rightMax - height[right] #calculate the amount of water able to be stored in the index
        return res








        return res
