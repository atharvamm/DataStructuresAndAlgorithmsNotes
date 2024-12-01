
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = -float('inf')
        start,end = 1,1

        for i in range(len(nums)):
            start *= nums[i]
            end *= nums[len(nums) - 1 - i]

            max_product = max(start,end,max_product)

            if start == 0:
                start = 1
            if end == 0:
                end = 1

        return max_product

obj = Solution()
print(obj.maxProduct([2,3,-2,4]))
print(obj.maxProduct([-2,0,-1]))