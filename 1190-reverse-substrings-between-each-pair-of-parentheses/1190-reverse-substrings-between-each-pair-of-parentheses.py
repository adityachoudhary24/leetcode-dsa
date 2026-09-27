class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                temp = []

                while stack[-1] != '(':
                    temp.append(stack.pop())

                stack.pop()  # remove '('

                for x in temp:
                    stack.append(x)

        return ''.join(stack)