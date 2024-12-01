
class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palindromes(start, end):
            cnt = 0
            while start > -1 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
                cnt += 1
            return cnt
        
        count = 0
        for i in range(len(s)):
            count = count + count_palindromes(i,i) + count_palindromes(i,i+1)
        return count

obj = Solution()
print(obj.countSubstrings("abc"))
print(obj.countSubstrings("aaa"))