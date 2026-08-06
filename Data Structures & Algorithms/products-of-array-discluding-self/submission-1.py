class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # defines the length of the array
        res = [0] * n # result array creation
        pref = [0] * n # prefix array creation
        suff = [0] * n # suffix array creation

        pref[0] = suff[n - 1] = 1 # set the arrays to have 1 for catching of edge cases.
        for i in range(1, n): # for index in range of 1 to the length of the array
            pref[i] = nums[i - 1] * pref[i - 1] # prefix array index i is set to arguement array index - 1 times the prefix array index - 1 (if i equals 2 it would multiply the previous index by the next index.)
        for i in range(n - 2, -1, -1): # the reason for the n-2 is because we are using the +1 to get the previous index which in this case is the next index so its a reversal logic.
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res
        