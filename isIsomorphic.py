class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check = {}
        for i in range(len(s)):
            if s[i] not in check:
                check[s[i]] = t[i]
            if check[s[i]] != t[i]:
                return False

        return len(check.values()) == len(set(check.values()))