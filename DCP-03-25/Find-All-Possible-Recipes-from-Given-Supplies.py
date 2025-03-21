class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        cooked, res = [False] * n, []
        supply_map = set(supplies)
        new_ing = True
        while(new_ing):
            new_ing = False
            for i in range(n):
                if cooked[i]:
                    continue

                if len(set(ingredients[i]) - supply_map) == 0:
                    res.append(recipes[i])
                    cooked[i] = new_ing = True
                    supply_map.add(recipes[i])

        return res
