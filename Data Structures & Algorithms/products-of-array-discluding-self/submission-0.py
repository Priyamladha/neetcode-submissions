class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix =[1]*len(nums), [1]*len(nums)

        for i in range(1, len(nums)):
            # print(prefix[i-1],nums[i-1])
            prefix[i] = prefix[i-1]*nums[i-1]
        # print(prefix)
        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j+1]*nums[j+1]

        # print(prefix, suffix)
        ans = []

        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])

        return ans