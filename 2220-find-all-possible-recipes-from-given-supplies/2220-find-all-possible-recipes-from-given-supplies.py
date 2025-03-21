class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        incoming = defaultdict(int)
        n = len(recipes)

        for i in range(n):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                incoming[recipes[i]] += 1

        queue = deque(supplies)
        ans = []
        while queue:

            node = queue.popleft()
            for neigh in graph[node]:

                incoming[neigh] -= 1
                if incoming[neigh] == 0:
                    ans.append(neigh)
                    queue.append(neigh)

        return ans