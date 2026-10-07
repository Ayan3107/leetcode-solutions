from collections import deque


class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            balance = 0

            for char in string:
                if char == "(":
                    balance += 1

                elif char == ")":
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}
        found = False
        result = []

        while queue:
            current = queue.popleft()

            if is_valid(current):
                result.append(current)
                found = True

            if found:
                continue

            for i in range(len(current)):
                if current[i] not in "()":
                    continue

                next_string = current[:i] + current[i + 1:]

                if next_string not in visited:
                    visited.add(next_string)
                    queue.append(next_string)

        return result
