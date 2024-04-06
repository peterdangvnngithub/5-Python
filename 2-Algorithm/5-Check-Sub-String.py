class Solution:
    def isSubString(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        else:
            for i in range(len(s2) - 1):
                if s1[0] == s2[i] and len(s2) - 1 >= len(s1) + i:
                    if s1 == s2[i: len(s1) + 1]:
                        return True
        return False
    
solution = Solution()
print(solution.isSubString("abc"   , "xabcyz"))
print(solution.isSubString("xabcyz", "abc"))