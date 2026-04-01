class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i, n in enumerate(nums): # i is the key and n is number value in the dict 
            diff = target - n        # so we make an equation for target - n = x to see if x is in the hashmap
            if diff in result:
                return [result[diff], i] # if it is in the dict return the index and value.
            result[n] = i # update the dict at the end everytime.
        return {}
