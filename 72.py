#had to search this one up but implemented levenshtein distance
#how does leetcode grading work???
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) + 1
        n = len(word2) + 1
        distances = [[0] * n for j in range(m)]
        for i in range(m):
            distances[i][0] = i
        
        for i in range(n):
            distances[0][i] = i
            
        for i in range(1, m):
            for j in range(1, n):
                if word1[i - 1] == word2[j - 1]:
                    distances[i][j] = distances[i - 1][j - 1]
                else:
                    distances[i][j] = min(distances[i][j - 1], distances[i - 1][j], distances[i - 1][j - 1]) + 1
        return int(distances[-1][-1])