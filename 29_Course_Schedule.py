"""
    Course Schedule

    Q. There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

        Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
        which is expressed as a pair: [0,1]

        Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all
        courses?

        Example 1:

        Input: numCourses = 2, prerequisites = [[1,0]]
        Output: true
        Explanation: There are a total of 2 courses to take.
                     To take course 1 you should have finished course 0. So it is possible.

        Example 2:

        Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
        Output: false
        Explanation: There are a total of 2 courses to take.
                     To take course 1 you should have finished course 0, and to take course 0 you should
                     also have finished course 1. So it is impossible.

        Constraints:

        The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how
        a graph is represented.
        You may assume that there are no duplicate edges in the input prerequisites.
        1 <= numCourses <= 10^5

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(set)
        for i, j in prerequisites:
            self.graph[i].add(j)
        n = numCourses
        self.visited = [0] * n
        self.flag = 0

        def dfs(s):
            if self.flag == 1:
                return
            if self.visited[s] == 1:
                self.flag = 1
            if self.visited[s] == 0:
                self.visited[s] = 1
                for each in self.graph[s]:
                    dfs(each)
                self.visited[s] = 2

        for i in range(n):
            if self.flag == 1:
                break
            if self.visited[i] == 0:
                dfs(i)
        return self.flag == 0
