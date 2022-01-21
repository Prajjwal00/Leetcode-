class Solution:    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff_total=0
        for i in range(len(gas)):
            diff_total+= gas[i]-cost[i]
        if diff_total<0:
            return -1
        else:
            start,tank=0,0
            for i in range(len(gas)):
                tank=tank +gas[i]-cost[i]
                if tank<0:
                    start=i+1
                    tank=0
            return start
