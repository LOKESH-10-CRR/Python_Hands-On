class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dt = {}
        for st in strs:
            key = ''.join(sorted(st))
            if key not in dt:
                dt[key] = []
            dt[key].append(st)
        return list(dt.values())

        