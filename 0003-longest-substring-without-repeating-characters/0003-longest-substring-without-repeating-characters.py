class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      
        left = 0
        my_dict = {}
        max_length = 0
        for right in range(len(s)):
            while s[right] in my_dict:
                my_dict[s[left]] -= 1
                if my_dict[s[left]] == 0:
                    del my_dict[s[left]]

                left += 1

            max_length = max(max_length, right - left + 1)
            my_dict[s[right]] = 1

        return max_length




