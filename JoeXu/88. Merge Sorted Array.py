class Solution(object):
    def merge(self, A, m, B, n):
        indexA = m-1;
        indexB = n-1;
        while indexA >=0 and indexB>=0:
            if A[indexA] > B[indexB]:
                A[indexA+indexB+1] = A[indexA]
                indexA -= 1
            else:
                A[indexA+indexB+1] = B[indexB]
                indexB -= 1
        while indexB>=0:
            A[indexB]=B[indexB]
            indexB-=1