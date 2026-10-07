
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = right = 0


        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        ans = set()
        n = len(s)

 
        def dfs(i, l, r, balance, path):
            if n - i < l + r:
                return

            if balance < 0:
                return

            if i == n:
                if l == 0 and r == 0 and balance == 0:
                    ans.add(path)
                return

            ch = s[i]

      
            if ch == '(' and l > 0:
                dfs(i + 1, l - 1, r, balance, path)


            if ch == ')' and r > 0:
                dfs(i + 1, l, r - 1, balance, path)

   
            if ch == '(':
                dfs(i + 1, l, r, balance + 1, path + ch)
            elif ch == ')':
                dfs(i + 1, l, r, balance - 1, path + ch)
            else:
                dfs(i + 1, l, r, balance, path + ch)

        dfs(0, left, right, 0, "")
        return list(ans)