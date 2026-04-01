class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #ensures that new entries are auto added into the list
        for s in strs: # for string in strs list
            count = [0] * 26 # this creates 26 indexes for an array each for a letter in the alphabet
            for c in s: # for character in string
                count[ord(c) - ord('a')] += 1 #ensures that the ascii value is between 0-25
            res[tuple(count)].append(s)
        return list(res.values())
            

        