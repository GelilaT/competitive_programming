class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        def score(left,right,score1,score2,turn):
            if left > right:
                return score1 >= score2

            if turn:

                choice1=score(left + 1, right, score1 + nums[left], score2, 0)
                choice2=score(left, right - 1, score1 + nums[right], score2, 0)

                return choice1 or choice2

            else:

                choice1=score(left + 1, right, score1, score2 + nums[left], 1)
                choice2=score(left, right - 1, score1, score2 + nums[right], 1)

                return choice1 and choice2

        return score(0, len(nums) - 1, 0, 0, 1)
