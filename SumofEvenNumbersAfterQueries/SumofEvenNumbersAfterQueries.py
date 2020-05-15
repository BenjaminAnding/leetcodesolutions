class Solution(object): 
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        totals = []
        total = sum(x for x in A if x % 2 == 0)
        for i in range(len(queries)): 
            if A[queries[i][1]] % 2 == 0:
                total -= A[queries[i][1]]
            A[queries[i][1]] += queries[i][0]
            if A[queries[i][1]] % 2 == 0:
                total += A[queries[i][1]]
            totals.append(total)
        return totals
