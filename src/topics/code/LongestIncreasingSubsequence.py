

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def recurse(index,prev, curLen):
            if index == len(nums):
                return curLen
            
            max_greater,max_not_greater = -float('inf'),-float('inf')
            if nums[index] > prev:
                len_take = recurse(index+1,nums[index],curLen+1)
                len_not_take = recurse(index+1,prev,curLen)
                max_greater = max([len_take,len_not_take])
            else:
                len_take = recurse(index+1,nums[index],1)
                len_not_take = recurse(index+1,prev,curLen)
                max_not_greater = max([len_take,len_not_take])
            
            return max([max_greater,max_not_greater])
                
        return recurse(0,-float('inf'),0)
        # ans = []


    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        1. Are the two not takes different fundamentally ?
        2. There are some computations we do multiple times, can we avoid them ?
        '''

        def recurse(index,prev, curLen):
            if index == len(nums):
                return curLen
            
            if ans[index] != - 1:
                return ans[index]

            len_not_take = recurse(index+1,prev,curLen)
            len_take = -float('inf')
            if nums[index] > prev:
                len_take = recurse(index+1,nums[index],curLen+1)
            else:
                len_take = recurse(index+1,nums[index],1)
            max_not_greater = max([len_take,len_not_take])
            ans[index] = max_not_greater
            return ans[index]

        ans = [-1 for i in range(len(nums))]
        recurse(0,-float('inf'),0)
        return ans[0]
        




examples = [
    [10,9,2,5,3,7,101,18],
    [0,1,0,3,2,3],
    [7,7,7,7,7,7,7]
]

obj = Solution()
for example in examples:
    print(example, obj.lengthOfLIS(example))
