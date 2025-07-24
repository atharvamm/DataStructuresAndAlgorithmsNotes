
from typing import List
from help import timeit
class Solution:
    @timeit(5)
    def removeDuplicates(self, nums: List[int]) -> int:
        slow,fast = 0,1
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
        # print("Ans:",nums,end = "\n")
        return slow + 1



if __name__ == "__main__":
    test_cases = [
        [1,1,2],
        [0,0,1,1,1,2,2,3,3,4],
    ]
    obj = Solution()
    for case in test_cases:
        print(case, obj.removeDuplicates(case.copy()))


