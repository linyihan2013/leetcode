import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
        route = []
        def solve(start):
            while targets[start]:
                solve(targets[start].pop())
            route.append(start)
        solve('JFK')
        return route[::-1]