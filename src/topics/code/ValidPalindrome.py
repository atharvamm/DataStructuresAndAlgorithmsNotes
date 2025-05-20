
class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters = []
        for i in range(len(s)):
            if s[i].isalnum():
                characters.append(s[i].lower())
        
        start,end = 0,len(characters) - 1
        while start <= end:
            if characters[start] == characters[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -=1 
            else:
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start += 1
                    end -= 1
        return True

