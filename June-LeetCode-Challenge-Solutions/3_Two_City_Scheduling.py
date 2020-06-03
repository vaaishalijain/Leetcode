"""
    Two City Scheduling

    Q. There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is
       costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

        Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

        Example 1:

        Input: [[10,20],[30,200],[400,50],[30,20]]
        Output: 110
        Explanation:
        The first person goes to city A for a cost of 10.
        The second person goes to city A for a cost of 30.
        The third person goes to city B for a cost of 50.
        The fourth person goes to city B for a cost of 20.

        The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

        Note:

        1 <= costs.length <= 100
        It is guaranteed that costs.length is even.
        1 <= costs[i][0], costs[i][1] <= 1000

"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans, n = 0, len(costs) // 2
        arr = [(a - b) for a, b in costs]
        ordArr = sorted((val, key) for (key, val) in enumerate(arr))
        for j, i in ordArr[:n]:
            ans += costs[i][0]
        for j, i in ordArr[n:]:
            ans += costs[i][1]
        return ans
