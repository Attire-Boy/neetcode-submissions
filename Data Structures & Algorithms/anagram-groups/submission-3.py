class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ##default dictionary
        res = defaultdict(list)
        ##iterating through list
        for s in strs:
            ## wherever '' use it to glue back together the word  e,a,t becomes eat 
            sortedS = ''.join(sorted(s))
            ##putting sorted string into the default dictionary
            res[sortedS].append(s)
        return list(res.values())