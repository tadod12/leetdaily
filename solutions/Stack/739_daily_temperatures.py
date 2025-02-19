class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # 90.95%
        monotonic_stack, res = [], [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while monotonic_stack and t > temperatures[monotonic_stack[-1]]:
                index = monotonic_stack.pop()
                res[index] = i - index
            monotonic_stack.append(i)
        return res
