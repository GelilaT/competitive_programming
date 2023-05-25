class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_dict = {5: 0, 10: 0, 20: 0}
        n = len(bills)
        for bill in bills:
            if bill == 5:
                bill_dict[5] += 1
            if bill == 10:
                if bill_dict[5] == 0:
                    return False
                else:
                    bill_dict[5] -= 1
                    bill_dict[10] += 1
            if bill == 20:
                if (bill_dict[10] == 0 and bill_dict[5] < 3) or (bill_dict[10] != 0 and bill_dict[5] == 0):
                    return False
                else:
                    if bill_dict[10]:
                        bill_dict[10] -= 1
                        bill_dict[5] -= 1
                        bill_dict[20] += 1
                    else:
                        bill_dict[5] -= 3
                        bill_dict[20] += 1
        return True