class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        sDict, pDict = dict(), dict()
        for i in range(len(p)):
            pDict[p[i]] = 1 + pDict.get(p[i], 0)
            sDict[s[i]] = 1 + sDict.get(s[i], 0)
        
        result = []
        if pDict == sDict:
            result.append(0)

        l = 0
        for r in range(len(p), len(s)):
            sDict[s[r]] = 1 + sDict.get(s[r], 0)

            sDict[s[l]] -= 1
            if sDict[s[l]] == 0:
                del sDict[s[l]]
            l += 1
            if pDict == sDict:
                result.append(l) 
        return result
