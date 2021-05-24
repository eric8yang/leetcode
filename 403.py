#new use of defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = defaultdict(set)
        d[0].add(1)
        for i in stones:
            for jump in d[i]:
                d[i + jump].update((jump, jump - 1, jump + 1) if jump != 1 else (jump, jump + 1))
        return d[stones[-1]]
            
        