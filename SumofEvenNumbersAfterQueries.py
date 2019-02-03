class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        totals = []
        for i in queries:
            A[i[1]] += i[0]
            total = 0
            for i in A:
                if i % 2 == 0:
                    total += i
            totals.append(total)
        return totals
