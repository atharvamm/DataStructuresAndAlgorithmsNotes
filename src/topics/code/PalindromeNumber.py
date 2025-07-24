class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        store = 0
        reduce = x
        while reduce > 0:
            store = store * 10 + reduce % 10
            reduce = reduce // 10

        return store == x
        

