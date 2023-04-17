class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0    
        def backtrack(idx, cur):
            nonlocal max_len
            cur_string = "".join(cur)
            if len(cur_string) > len(set(cur_string)):
                return
            max_len = max(max_len, len(cur_string))
            for i in range(idx, len(arr)):
                backtrack(i + 1, cur + [arr[i]])

        backtrack(0, [])
        return max_len