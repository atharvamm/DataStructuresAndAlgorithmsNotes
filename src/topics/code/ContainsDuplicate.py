
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq_nums = set()
        for num in nums:
            if num not in uniq_nums:
                uniq_nums.add(num)
            else:
                return True
        return False
        