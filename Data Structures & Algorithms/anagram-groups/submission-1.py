class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        hm = {}
        for i in range(len(strs)):
            sortedStr = "".join(sorted(strs[i]))
            if sortedStr in hm:
                hm[sortedStr].append(i)
            else:
                hm[sortedStr] = [i]
        res = []
        for indexes in hm.values():
            temp=[]
            for idx in indexes:
                temp.append(strs[idx])
            res.append(temp)
        return res