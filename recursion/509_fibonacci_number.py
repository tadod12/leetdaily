class Solution(object):
    mem = {
        0: 0,
        1: 1,
    }

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in self.mem:
            return self.mem[n]
        else:
            self.mem[n] = self.fib(n-1) + self.fib(n-2)
            return self.mem[n]
