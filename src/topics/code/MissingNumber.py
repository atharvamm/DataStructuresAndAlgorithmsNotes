
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n*(n+1))//2 - sum(nums)
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_nums = list(range(len(nums) + 1))
        ans = expected_nums[0]

        for num in expected_nums[1:]:
            ans ^= num

        for num in nums:
            ans ^= num

        return ans
        