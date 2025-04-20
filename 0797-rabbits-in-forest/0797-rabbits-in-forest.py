class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        count = Counter(answers)
        rabbits = 0
        for key, val in count.items():
            while val > 0:
                rabbits += key + 1
                val -= (key + 1)

        return rabbits
