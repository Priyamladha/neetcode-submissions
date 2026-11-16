class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            tmp_sum = numbers[left]+numbers[right]

            if tmp_sum > target:
                right -=1
                continue

            if tmp_sum < target:
                left +=1
                continue

            if tmp_sum == target:
                return [left+1, right+1]

        return []