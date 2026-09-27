class Solution:
    def reverseParentheses(self, s):
        stack = []

        for char in s:
            if char == ')':
                current = []

                while stack[-1] != '(':
                    current.append(stack.pop())

                stack.pop()
                stack.extend(current)

            else:
                stack.append(char)

        return ''.join(stack)