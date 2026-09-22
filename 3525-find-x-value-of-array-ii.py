class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Each tree node:
        # [product % k, count of prefixes for each remainder]
        tree = [[0] * (k + 1) for _ in range(4 * n)]

        def make_leaf(value):
            node = [0] * (k + 1)

            remainder = value % k

            node[0] = remainder
            node[1 + remainder] = 1

            return node

        def merge(left, right):
            node = [0] * (k + 1)

            # Product of the entire combined segment
            node[0] = (left[0] * right[0]) % k

            # Prefixes entirely inside the left segment
            for r in range(k):
                node[1 + r] = left[1 + r]

            # Prefixes that use all of LEFT + a prefix of RIGHT
            for r in range(k):
                new_r = (left[0] * r) % k
                node[1 + new_r] += right[1 + r]

            return node

        def build(index, left, right):
            if left == right:
                tree[index] = make_leaf(nums[left])
                return

            mid = (left + right) // 2

            build(index * 2, left, mid)
            build(index * 2 + 1, mid + 1, right)

            tree[index] = merge(
                tree[index * 2],
                tree[index * 2 + 1]
            )

        def update(index, left, right, position, value):
            if left == right:
                tree[index] = make_leaf(value)
                return

            mid = (left + right) // 2

            if position <= mid:
                update(index * 2, left, mid, position, value)
            else:
                update(index * 2 + 1, mid + 1, right, position, value)

            tree[index] = merge(
                tree[index * 2],
                tree[index * 2 + 1]
            )

        def query(index, left, right, query_left, query_right):
            # Completely inside requested range
            if query_left <= left and right <= query_right:
                return tree[index]

            mid = (left + right) // 2

            if query_right <= mid:
                return query(
                    index * 2,
                    left,
                    mid,
                    query_left,
                    query_right
                )

            if query_left > mid:
                return query(
                    index * 2 + 1,
                    mid + 1,
                    right,
                    query_left,
                    query_right
                )

            left_result = query(
                index * 2,
                left,
                mid,
                query_left,
                query_right
            )

            right_result = query(
                index * 2 + 1,
                mid + 1,
                right,
                query_left,
                query_right
            )

            return merge(left_result, right_result)

        # Build the segment tree
        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Update nums[index]
            nums[index] = value
            update(1, 0, n - 1, index, value)

            # Query nums[start ... n-1]
            result = query(1, 0, n - 1, start, n - 1)

            # x-value
            answer.append(result[1 + x])

        return answer