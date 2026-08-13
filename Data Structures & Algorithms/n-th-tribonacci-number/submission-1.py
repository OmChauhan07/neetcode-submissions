class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        for i in range(2, n):
            t0, t1, t2 = t1, t2, t0 + t1 + t2

        return t2