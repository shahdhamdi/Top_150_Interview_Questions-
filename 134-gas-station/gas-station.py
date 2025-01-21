class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost)>sum(gas):
            return -1
        tank=0
        start=0
        n=len(gas)
        total_tank=0
        for i in range(n):
            tank+=gas[i]-cost[i]
            total_tank+=gas[i]-cost[i]
            if tank<0:
                tank=0
                start=i+1
        return start if total_tank>=0 else -1
            
        