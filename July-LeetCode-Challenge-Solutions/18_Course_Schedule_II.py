"""
    Course Schedule II

    Q. There are a total of n courses you have to take, labeled from 0 to n-1.

        Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is
        expressed as a pair: [0,1]

        Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should
        take to finish all courses.

        There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all
        courses, return an empty array.

        Example 1:

        Input: 2, [[1,0]]
        Output: [0,1]
        Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
                     course 0. So the correct course order is [0,1] .

        Example 2:

        Input: 4, [[1,0],[2,0],[3,1],[3,2]]
        Output: [0,1,2,3] or [0,2,1,3]
        Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
                     courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
                     So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
        Note:

        The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how
        a graph is represented.
        You may assume that there are no duplicate edges in the input prerequisites.

"""


class Solution:
    def findOrder(self, n: int, arr: List[List[int]]) -> List[int]:
        self.graph = defaultdict(set)
        for i, j in arr:
            self.graph[i].add(j)

        def topo(st):
            if self.flag:
                return
            if self.visited[st] == 1:
                self.flag = 1
            if self.visited[st] == 0:
                self.visited[st] = 1
                for j in self.graph[st]:
                    topo(j)
                self.visited[st] = 2
                self.ans.append(st)

        self.visited = [0] * n
        self.ans, self.flag = [], 0
        for i in range(n):
            if self.flag == 1:
                break
            if self.visited[i] == 0:
                topo(i)
        return [] if self.flag else self.ans
