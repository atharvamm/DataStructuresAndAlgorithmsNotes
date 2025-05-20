
class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        store = []
        closing_chars = {"{":"}","(":")","[":"]"}

        while s:
            if len(store) and closing_chars.get(s[-1],"") == store[-1]:
                    s.pop()
                    store.pop()
            else:
                store.append(s.pop())
        
        if len(store):
            return False
        return True
        