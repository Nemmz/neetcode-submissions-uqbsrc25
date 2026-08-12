class Solution:
    def isPalindrome(self, s: str) -> bool:
        front, end = 0, len(s) - 1

        while front < end: # we haven't reached the end yet
            while front < end and not s[front].isalnum(): # advance front if a non compareable character is encountered
                front += 1
            while end > front and not s[end].isalnum(): # advance end if a non compareable character is encountered
                end -= 1
            if s[front].lower() != s[end].lower(): # compare the two indexes with lowercase letters to see if they are the same
                return False
            front, end = front + 1, end - 1 #advance both pointers.
        return True
        
