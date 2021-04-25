class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        result = ""
        temp = ""
        for c in reversed(s):
            if c == '-':
                continue
            temp = c + temp
            if len(temp) == k:
                result = temp + '-' + result
                temp = ""
        if len(temp) > 0:   
            result = temp + '-' + result
        result = result[:-1]
        return result