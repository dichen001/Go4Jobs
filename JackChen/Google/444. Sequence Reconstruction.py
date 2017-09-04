"""
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true
UPDATE (2017/1/8):
The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings). Please reload the code definition to get the latest changes.

"""


import collections
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """

        "easier solution"
        idx = {n: i for i, n in enumerate([None] + org)}
        pairs = set(zip([None] + org, org))
        for seq in seqs:
            for a, b in zip([None] + seq, seq):
                if idx.get(a, -1) >= idx.get(b, -1):
                    return False
                pairs.discard((a, b))
        return not pairs



        "longer solution"
        # build topo first
        topo, in_degree = collections.defaultdict(set), collections.defaultdict(int)
        all_nodes = set()
        for seq in seqs:
            for i in range(len(seq)):
                all_nodes |= {seq[i]}
                if i == 0:
                    in_degree[seq[i]] += 0
                if i + 1 < len(seq) and seq[i+1] not in topo[seq[i]]:
                    topo[seq[i]].add(seq[i+1])
                    in_degree[seq[i+1]] += 1
        n = len(org)
        if len(all_nodes) != n:
            return False
        queue = [i for i in range(1, n + 1) if in_degree[i] == 0]
        reconstruct = []
        while len(queue) == 1:
            i = queue.pop()
            reconstruct += [i]
            for j in topo[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
        return len(queue) == 0 and reconstruct == org
        
s = Solution()
print s.sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]])