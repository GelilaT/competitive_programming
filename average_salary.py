class Solution:
    def average(self, salary: List[int]) -> float:
        minsal=min(salary)
        maxsal=max(salary)
        sums=0
        for i in range(len(salary)):
            sums+=salary[i]
        aver=(sums-maxsal-minsal)/(len(salary)-2)
        return aver

