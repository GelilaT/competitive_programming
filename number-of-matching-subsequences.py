class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        index = defaultdict(list)
        for i, char in enumerate(s):
            index[char].append(i)

        ans = 0
        for word in words:
            pre = 0
            for i in range(len(word)):
                val = index[word[i]]
                idx = bisect_left(val, pre)

                if idx < len(val):
                    if index[word[i]][idx] < pre:
                        break

                    else:
                        pre = index[word[i]][idx] + 1
                
                else:
                    break

            else:

                ans += 1

        return ans