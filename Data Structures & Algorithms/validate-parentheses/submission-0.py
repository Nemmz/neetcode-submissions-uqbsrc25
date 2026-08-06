class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        isOpen = {")": "(", "]" : "[" , "}" : "{" }

        for char in s:
            if char in isOpen:
                if result and result[-1] == isOpen[char]:
                    result.pop()
                else:
                    return False
            else:
                result.append(char)

        return True if not result else False
            

