class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
            prefixsum=[]
            prefix=0
            for j in range(len(chalk)):
                prefix+=chalk[j]
                prefixsum.append(prefix)
            freq=k%prefixsum[-1]
            for j in range(len(chalk)):
                if freq>=chalk[j]:
                    freq-=chalk[j]
                else:
                    return j