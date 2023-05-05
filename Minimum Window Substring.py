class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_dict = Counter(t)
        # for i in range(len(t)):
        #    t_dict[t[i]] += 1 
        
        res = [len(s), ""]
        string = ""
        s_dict = Counter()
        left = 0
        min_len = inf
        for right in range(len(s)):
            string += s[right]
            if s[right] in t:
                s_dict[s[right]] += 1 
            while t_dict <= s_dict:
                res = min([(right - left), string[left:]], res)
                if t_dict[s[left]]:
                    s_dict[s[left]] -= 1
                    # if s_dict[s[left]] == 0:
                    #     del s_dict[s[left]]
                left += 1
        return res[1]
