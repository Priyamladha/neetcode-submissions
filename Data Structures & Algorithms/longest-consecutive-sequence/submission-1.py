class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        ans = 0
        for num in nums:
            if (num-1) in hashset:
                continue
            length = 1
            while (num+length) in hashset:
                length +=1
            ans = max(ans, length)

        return ans
            
