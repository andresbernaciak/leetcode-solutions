class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j, rest in enumerate(nums[i+1:]):
                if num + rest == target:
                    return [i, i+j+1]
