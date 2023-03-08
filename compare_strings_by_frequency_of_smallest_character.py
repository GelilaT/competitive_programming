class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
       
        length = len(words)
        words = sorted(word.count(min(word)) for word in words)
        ans = [0] * len(queries)
        for i, query in enumerate(queries):
            freq = query.count(min(query))
            low = 0 
            high = len(words) - 1
            while low <= high:
                mid = low + (high - low)//2
                if words[mid] <= freq:
                    low = mid + 1
                else:
                    high = mid - 1
            ans[i] = length - low
        return ans
