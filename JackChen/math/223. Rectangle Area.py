"""

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        s1 = (C-A)*(D-B)
        s2 = (G-E)*(H-F)
        left = max(A,E)
        right = max(min(C,G), left);
        bottom = max(B,F)
        top = max(min(D,H), bottom);
        ss = (right-left)*(top-bottom)
        return s1+s2-ss
