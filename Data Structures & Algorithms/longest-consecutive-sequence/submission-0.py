class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        ans = 0
        for num in nums:
            if (num-1) in hashset:
                continue
            tmp = 1
            seq = num+1
            while seq in hashset:
                tmp +=1
                seq +=1
            ans = max(ans, tmp)

        return ans
            
