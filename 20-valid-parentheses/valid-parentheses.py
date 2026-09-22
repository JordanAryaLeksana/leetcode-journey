class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in "([{":
                res.append(char)
            else:
                if not res:
                    return False

                top = res[-1]

                if top == pairs[char]:    
                    res.pop()
                else:
                    return False

        return not res

       
