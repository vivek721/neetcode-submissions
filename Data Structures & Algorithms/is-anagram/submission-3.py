class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) < len(t):
            s,t=t,s
        print(t,s)
        for str in t:
            s = s.replace(str,"",1)

        return len(s) == 0