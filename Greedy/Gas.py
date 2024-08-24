# 134. Gas Station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total_tank, curr_tank, = 0, 0
        starting_position = 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                curr_tank = 0
                starting_position = i + 1
        return starting_position if total_tank >= 0 else -1
