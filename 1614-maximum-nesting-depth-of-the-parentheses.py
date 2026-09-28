class Solution:
    def maxDepth(self, s):
        depth = 0
        answer = 0

        for ch in s:
            if ch == '(':
                depth+=1
                answer=max(answer, depth)

            elif ch == ')':
                depth-=1

        return answer            