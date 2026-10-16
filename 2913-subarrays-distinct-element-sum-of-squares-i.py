class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        size = 4 * n
        sum_d = [0] * size
        sum_sq = [0] * size
        lazy = [0] * size

        def apply(node, length, add):
            sum_sq[node] += 2 * add * sum_d[node] + add * add * length
            sum_d[node] += add * length
            lazy[node] += add

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            add = lazy[node]

            apply(node * 2, mid - left + 1, add)
            apply(node * 2 + 1, right - mid, add)

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, right - left + 1, 1)
                return

            push(node, left, right)

            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            sum_d[node] = sum_d[node * 2] + sum_d[node * 2 + 1]
            sum_sq[node] = sum_sq[node * 2] + sum_sq[node * 2 + 1]

        last = {}
        ans = 0

        for r, value in enumerate(nums):
            left = last.get(value, -1) + 1
            update(1, 0, n - 1, left, r)

            ans = (ans + sum_sq[1]) % MOD

            last[value] = r

        return ans