class Solution:
    def isValid(self, s: str) -> bool:
        pair = dict(('()', '[]', '{}'))
        stack = []
        for c in s:
            # if current character is an opening parentheses
            if c in '([{':
                # treat list as a stack and remove the first item
                stack.append(c)
            # if current char is a closing bracket and stack is empty then return False
            elif len(stack) == 0 or c != pair[stack.pop()]:
                return False

        # if stack is empty then true else false
        return len(stack) == 0

    
