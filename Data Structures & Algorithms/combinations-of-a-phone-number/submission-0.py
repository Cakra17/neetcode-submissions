class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if not digits:
            return []

        res = []
        stack = []

        def dfs(i):
            if i >= len(digits): 
                res.append("".join(stack))
                return
            
            for c in keyboard[digits[i]]:
                stack.append(c)
                dfs(i+1)
                stack.pop()

        dfs(0)
        return res
        