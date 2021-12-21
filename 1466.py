#crazy bad solution
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import deque
        res = 0
        visited = [False] * n
        adj = [set() for _ in range(n)]
        paths = set()
        for path in connections:
            paths.add((path[0], path[1]))
            adj[path[0]].add(path[1])
            adj[path[1]].add(path[0])
        q = deque()
        q.append(0)
        while q:
            curr = q.popleft()
            visited[curr] = True
            print(curr)
            for end in adj[curr]:
                if not visited[end]:
                    print(curr, end)
                    q.append(end)
                    if (end, curr) not in paths:
                        print(True)
                        res += 1            
        return res

#better solution, this is average O(n) worst (O(n^2)), for some reason leetcode won't accept it for me when it's literally the best answer
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        q = deque(connections)
        connected = {0}
        while q:
            u, v = q.popleft()
            if v in connected:
                connected.add(u)
            elif u in connected:
                connected.add(v)
                res += 1
            else:
                q.append([u,v])
        return res