class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}

        left, right = 0, 0
        maxString = 0
        while right < len(s):
            if s[right] in hashmap:
                maxString = max(maxString, right - left)
                while s[right] in hashmap:
                    hashmap.pop(s[left])
                    left +=1
            else:
                hashmap[s[right]] = right
                right +=1

        if hashmap:
            maxString = max(maxString, len(hashmap))
        return maxString
