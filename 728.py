#i found that 
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            digits = []
            curr = i
            while curr > 0:
                digits.append(curr % 10)
                curr //= 10
            add = True
            for digit in digits:
                if digit == 0 or i % digit != 0:
                    add = False
                    break
            if add:
                res.append(i)
        return res