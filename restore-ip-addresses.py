class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def isvalid(cur):
            if cur[0] == '0' and len(cur) > 1  or int(cur) > 255:
                return False
            return True
        ans = []
        def backtrack(idx, ip, dots):
            if idx == len(s) and dots == 4:
                ans.append(ip[:-1])
                return
            
            for i in range(idx, min(idx + 3, len(s))):
                cur = s[idx : i + 1]
                if isvalid(cur):
                    backtrack(i + 1, ip + cur + '.',dots + 1) 
            
        backtrack(0, '', 0)
        return ans