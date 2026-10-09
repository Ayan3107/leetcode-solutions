class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed = 0

        for char in s:
            if char == '(':
                # Closing parentheses must come in pairs.
                if needed % 2 == 1:
                    insertions += 1
                    needed -= 1

                needed += 2

            else:
                needed -= 1

                # No opening parenthesis is available.
                if needed < 0:
                    insertions += 1
                    needed = 1

        return insertions + needed
