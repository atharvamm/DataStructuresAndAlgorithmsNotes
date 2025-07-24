
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        # # Brute
        # for _ in range(k):
        #     x = nums.pop()
        #     nums.insert(0,x)

        # Beter
        store = []
        for i in range(-k, 0, 1):
            store.append(nums[i])
        
        for i in range(len(nums) - k - 1,-1,-1):
            nums[i + k] = nums[i]
        
        for i in range(len(store) - 1,-1,-1):
            nums[i] = store[i]

        # # Optimal
        # k = k % len(nums)
        # for start,end in [[0,len(nums) - 1], [0,k -1],[k,len(nums) - 1]]:
        #     while start < end:
        #         nums[start],nums[end] = nums[end],nums[start]
        #         start += 1
        #         end -= 1

        
        

obj = Solution()
testcases = [
    [[1,2,3,4,5,6,7], 3],
    [[-1,-100,3,99], 2]
]

for test_case in testcases:
    use = test_case[0].copy()
    obj.rotate(use, test_case[1])
    print(test_case[0], use)
