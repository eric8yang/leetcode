class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = set()
        for fold in folder:
            parts = fold.split('/')
            if len(parts) == 2:
                res.add(fold)
            else:
                add = True
                for i in range(2, len(parts)):
                    pre = '/'.join(parts[:i])
                    if pre in res:
                        add = False
                        break
                if add:
                    res.add(fold)
        res = list(res)
        return res