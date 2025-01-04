class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = defaultdict(list)

        for index, char in enumerate(s):
            if char not in count:
                count[char].extend([index, 0])
            else:
                count[char][1] = index

        palindrom_count = 0

        for char in count:
            i, j = count[char]
            if i < j:
                palindrom_count += len(set((s[i + 1:j])))


        return palindrom_count