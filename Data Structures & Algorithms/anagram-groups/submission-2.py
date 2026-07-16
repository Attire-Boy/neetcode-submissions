class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ##default dictionary
        res = defaultdict(list)
        ##iterating through list
        for s in strs:
            ##appending space before a sorted string
            sortedS = ''.join(sorted(s))
            ##putting sorted string into the default dictionary
            res[sortedS].append(s)
        return list(res.values())