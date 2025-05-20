

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def get_char_count(string):
            string_chars = {}
            for character in string:
                if character not in string_chars:
                    string_chars[character] = 0
                string_chars[character] += 1
            string_chars = {key: string_chars[key] for key in sorted(string_chars)}
            return string_chars
        
        s_chars = get_char_count(s)
        t_chars = get_char_count(t)

        if s_chars == t_chars:
            if s_chars.items() == t_chars.items():
                return True
        return False