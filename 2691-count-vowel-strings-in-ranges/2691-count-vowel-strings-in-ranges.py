class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        prefix = [0] * (len(words) + 1)
        running = 0
        for idx, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                running += 1
            
            prefix[idx + 1] = running

        ans = []
        print(prefix)
        for start, end in queries:
            res = prefix[end + 1] - prefix[start]
            ans.append(res)

        return ans


        