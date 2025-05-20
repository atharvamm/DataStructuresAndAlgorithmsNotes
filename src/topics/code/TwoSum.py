
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        answers = {}
        for i in range(len(nums)):
            cur_target = target - nums[i]
            if cur_target in answers:
                return [i,answers[cur_target]]
            else:
                answers[nums[i]] = i

# Example usage:
obj = Solution()
print(obj.twoSum([2,7,11,15],9))
print(obj.twoSum([3,2,4],6))
print(obj.twoSum([3,3],6))