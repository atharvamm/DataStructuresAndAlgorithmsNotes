
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,end = 0,0
        characters = set()
        max_len = 0

        while end < len(s):
            if s[end] in characters:
                max_len = max(max_len, len(characters))

                while s[end] in characters:
                    characters.remove(s[start])
                    start += 1
            characters.add(s[end])
            end += 1
        max_len = max(max_len, len(characters))
        return max_len