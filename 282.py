#got some inspiration from discord group, but this was good practice of some new python techniques
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        arr = [(0, int(num[0]), int(num[0]), num[0])] #sum, mult, last mult, expression
        res = []
        for i in num[1:]:
            n = int(i)
            newArr = []
            for (currSum, currMult, lastMult, exp) in arr:
                newArr.append((currSum + currMult, n, n, exp + f"+{i}"))
                newArr.append((currSum + currMult, -n, -n, exp + f"-{i}"))
                newArr.append((currSum, n * currMult, n, exp + f"*{i}"))
                if lastMult > 0:
                    newLast = lastMult * 10 + n;
                    newArr.append((currSum, currMult / lastMult * newLast, newLast, exp + i))
                elif lastMult < 0:
                    newLast = lastMult * 10 - n;
                    newArr.append((currSum, currMult / lastMult * newLast, newLast, exp + i))
            arr = newArr
        
        for (currSum, currMult, lastMult, exp) in arr:
            if currSum + currMult == target:
                res.append(exp) 
        
        return res
        