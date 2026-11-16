class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            tmp = target - nums[i]

            if tmp in hashmap and hashmap[tmp] != i:
                return [hashmap[tmp], i]
            else:
                hashmap[nums[i]] = i

        return []