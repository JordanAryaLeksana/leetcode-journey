class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for char in s:
            if char == "(":
                res.append(char)
            elif char == "[":
                res.append(char)
            elif char == "{":
                res.append(char)
            else:
                pairs = {")": "(", "]": "[", "}": "{"}
                if not res:
                    return False

                top = res[-1]

                if top == pairs[char]:    
                    res.pop()
                else:
                    return False

        return not res

       
