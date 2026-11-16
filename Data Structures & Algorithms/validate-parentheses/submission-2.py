class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {']':'[','}':'{',')':'('}
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                latest = stack.pop()
                if hashmap.get(c) != latest:
                    return False
        if len(stack) > 0:
            return False
        return True