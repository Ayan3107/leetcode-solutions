class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def get_day(date):
            month = int(date[:2])
            day = int(date[3:])
            total = 0

            for i in range(month - 1):
                total += days[i]

            return total + day

        alice_start = get_day(arriveAlice)
        alice_end = get_day(leaveAlice)
        bob_start = get_day(arriveBob)
        bob_end = get_day(leaveBob)

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        if start > end:
            return 0

        return end - start + 1
