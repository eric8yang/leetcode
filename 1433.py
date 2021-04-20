class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            elif s1[i] < s2[i]:
                s2, s1 = s1, s2
                break
        for i in range(len(s1)):
            print(s1[i] + " " + s2[i])
            if s1[i] < s2[i]:
                return False
        return True