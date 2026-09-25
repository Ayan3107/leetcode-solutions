class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def union(a, b):
            return a | b

        def product(a, b):
            return {x + y for x in a for y in b}

        def parse_expr(i):
            result = set()

            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    i += 1
                    continue

                current, i = parse_term(i)
                result = union(result, current)

            return result, i

        def parse_term(i):
            result = {""}

            while i < len(expression) and expression[i] not in '},':
                if expression[i] == '{':
                    current, i = parse_expr(i + 1)
                    i += 1
                else:
                    current = {expression[i]}
                    i += 1

                result = product(result, current)

            return result, i

        result, _ = parse_expr(0)

        return sorted(result)