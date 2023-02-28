class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        arr=[0] * (n+1)
        for shift in shifts:

            start=shift[0]
            end=shift[1]
            direction=shift[2]
            if direction == 1:
                arr[start] += 1
                arr[end+1] -= 1
            else:
                arr[start] -= 1
                arr[end+1] += 1

        prefix=0
        for i in range(len(arr)):
            prefix += arr[i]
            arr[i]=prefix

        ans=""
        for i in range(len(arr) - 1):

            ans += chr(((ord(s[i])+ arr[i] - 97) % 26)  + 97)

        return ans
