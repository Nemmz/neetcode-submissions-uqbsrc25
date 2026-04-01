class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # defines the length of the array
        res = [0] * n # result array creation
        pref = [0] * n # prefix array creation
        suff = [0] * n # suffix array creation

        pref[0] = suff[n - 1] = 1 # set the arrays to have 1 for catching of edge cases.
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res
        