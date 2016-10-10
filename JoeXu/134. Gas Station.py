class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start=0
        rest=0
        if sum(gas)<sum(cost):
            return -1
        for i in range(len(gas)):
            if gas[i]+rest-cost[i]<0:
                rest=0
                start=i+1
            else:
                rest=rest+gas[i]-cost[i]
        return start