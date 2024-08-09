# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)

        for word in strs:
            sort = ''.join(sorted(word))
            ana_map[sort].append(word)
        
        return list(ana_map.values())
