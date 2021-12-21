#almost gs algorithm hm
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        res = 0
        match = dict()
        for start, end in pairs:
            match[start] = [end, preferences[start].index(end)]
            match[end] = [start, preferences[end].index(start)]
        for start in range(n):
            rating = match[start][1]
            for end in preferences[start][:rating]:
                if preferences[end].index(start) < match[end][1]:
                    res += 1
                    break
        return res