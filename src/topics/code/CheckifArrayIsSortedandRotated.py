
from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        breakpoint = -1
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1)%len(nums)]:
                breakpoint = i + 1
                break
        print(breakpoint)
        for i in range(len(nums) - 1):
            if nums[(i + breakpoint)%len(nums)] <= nums[(i + 1 + breakpoint)%len(nums)]:
                pass
            else:
                return False
        return True
        

