class Solution:
    def evaluate(self, s, knowledge):
        values = dict(knowledge)
        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                i += 1
                key = ""

                while s[i] != ')':
                    key += s[i]
                    i += 1

                result.append(values.get(key, "?"))
                i += 1
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)