class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        my_dict = {}
        left = 0
        ans = 0
        for right in range(len(s)):
            my_dict[s[right]] = my_dict.get(s[right], 0) + 1
            
            while len(my_dict) == 3:
                ans += len(s) - right
                my_dict[s[left]] -= 1
                if my_dict[s[left]] == 0:
                    del my_dict[s[left]]

                left += 1

        return ans

            

            

