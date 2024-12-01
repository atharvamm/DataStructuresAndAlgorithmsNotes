
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(start,end):
            while start > -1 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1:end],end - start - 1

        max_len = 0
        palindrome_string = ""
        for i in range(len(s)):
            string, length = palindrome(i,i)
            if length > max_len:
                palindrome_string = string
                max_len = length
            string, length = palindrome(i,i+1)
            if length > max_len:
                palindrome_string = string
                max_len = length
        
        return palindrome_string