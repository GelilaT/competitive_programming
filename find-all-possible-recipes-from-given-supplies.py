class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        queue = deque(supplies)
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                    graph[ingredients[i][j]].append(recipes[i])
                    in_degree[recipes[i]] += 1
        
        done = []
        # print(graph)
        while queue:
            # print(queue)
            ingred = queue.popleft()
            for adj in graph[ingred]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                        queue.append(adj)
                        done.append(adj)
        return done