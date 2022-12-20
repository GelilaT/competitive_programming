class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        broken=False
        minlen=len(min(strs,key=len))
        for i in range(minlen):
            for words in strs:
                if words[i]!=strs[0][i]:
                    broken=True
                    break
            else:
                prefix+=strs[0][i]
            if broken:
                break
        return prefix
