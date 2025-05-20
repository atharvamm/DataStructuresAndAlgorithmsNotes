
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_con = 0
        for num in nums:
            if num + 1 not in set_nums:
                cur_num = num
                while cur_num in set_nums:
                    cur_num -= 1
                max_con = max(max_con, num - cur_num)        
        return max_con 