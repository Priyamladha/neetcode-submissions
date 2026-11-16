class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}

        left = 0
        maxString = 0
        for right in range(len(s)):
            while s[right] in hashmap:
                hashmap.pop(s[left])
                left +=1
            
            hashmap[s[right]] = right
            maxString = max(maxString, right - left + 1)

        return maxString
