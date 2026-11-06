class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        count = {}
        ans = [0] * len(queries)

        left = 0
        right = 0

        for q, index in sorted_queries:
            # Add requests that happened at or before q
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                count[server] = count.get(server, 0) + 1
                right += 1

            # Remove requests that happened before q - x
            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            # Servers with no requests in the interval
            ans[index] = n - len(count)

        return ans
