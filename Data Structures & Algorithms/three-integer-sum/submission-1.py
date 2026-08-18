class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # this prevents duplicates since our array is sorted if two -1 are next to each other we can skip it since we already checked it.
            left, right = i + 1, len(nums) - 1
            while left < right: # stay in the loops until left becomes more than left.
                total = nums[i] + nums[left] + nums[right] # the resulting total
                if total < 0: # if total is less than 0 move the left pointer more to the right since bigger values are towards the right
                    left += 1
                elif total > 0: # if total is more than 0 move the right pointer more to the left since smaller values are towards the left.
                    right -= 1
                else: # a zero result was found now add it to a result list
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: #advance the left pointer to avoid duplicates since our list is sorted
                        left += 1
                    while left < right and nums[right] == nums[right - 1]: #advance the right pointer to avoid duplicates since our list is sorted
                        right -= 1
                    left += 1 #  advnace the pointer to see the first new
                    right -= 1 # advnace the pointer to see the first new
        return result


