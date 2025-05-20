
from typing import List
class Solution:
    # Brute Force
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                cur_area = min(height[j],height[i]) * (j - i)
                max_area = max(cur_area, max_area)
        
        return max_area

    # O(n) : Linear Time
    def maxArea(self, height: List[int]) -> int:
        start,end = 0,len(height) - 1
        cur_area,max_area = 0,0

        while start < end:
            cur_area = min(height[end], height[start]) * (end - start)
            max_area = max(max_area, cur_area)

            if height[end] < height[start]:
                end -= 1
            else:
                start += 1
        
        return max_area


obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(obj.maxArea([1,8,6,2,5,4,3,8,7])) # 49
print(obj.maxArea([1,1]))
print(obj.maxArea([1,2,1])) # 2