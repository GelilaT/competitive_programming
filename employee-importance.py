"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total = 0
        def dfs(target):
            nonlocal total
            for i, cur in enumerate(employees):
                if cur.id == target:
                    idx = i
                    break
            total += employees[idx].importance
            for neighbours in employees[idx].subordinates:
                dfs(neighbours)
        dfs(id)
        return total