class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front, end = 0, len(numbers) - 1
        while front < end: #ensures that we won't pass the other pointer if the situation goes that long
            if (numbers[front] + numbers[end] == target) is True: 
                return [front+1, end+1] # returns the indexes if the target is meet
            elif numbers[front] + numbers[end] < target: # advances the front pointer if the number is bigger than the target
                front += 1 # Note this only works on decreasing list otherwise would fail.
            else:
                end -= 1
        