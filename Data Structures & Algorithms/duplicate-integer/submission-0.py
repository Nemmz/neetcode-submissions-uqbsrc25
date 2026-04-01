class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_Dups = set({})
        for i in nums:
            non_Dups.add(i)
        if(len(non_Dups) != len(nums)):
            return True
        else:
            return False
