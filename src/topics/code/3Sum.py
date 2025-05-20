
from typing import List
class Solution:
    def threeSum_brute(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if i!=j and j!=k and i!=k and (nums[i]+nums[j]+nums[k] == 0):
                        cur_list = [nums[i],nums[j],nums[k]]
                        if cur_list not in answer:
                            answer.append(cur_list)        
        return answer
    
    def threeSum(self,nums: List[int]) -> List[List[int]]:
        answers = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            start,end = i+1,len(nums)
            while start < end:
                if (nums[i] + nums[start] + nums[end] == 0):
                    if [nums[i],nums[start],nums[end]] not in answers:
                        answers.append([nums[i],nums[start],nums[end]])
        
        return answers


