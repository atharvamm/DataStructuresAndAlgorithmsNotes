
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_ptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[num_ptr] = nums[i]
                num_ptr += 1
        for i in range(num_ptr,len(nums)):
            nums[i] = 0
        