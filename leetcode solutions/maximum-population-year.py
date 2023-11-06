class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        years = [0] * 101

        for log in logs:
            birth = log[0] - 1950
            death = log[1] - 1950

            for i in range(birth, death):
                years[i] += 1

        maxpop = 0
        idx = 0
        for i, pop in enumerate(years):
            if pop > maxpop:
                maxpop = pop
                idx = i

        return idx + 1950



        

