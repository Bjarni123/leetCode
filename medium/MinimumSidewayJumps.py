class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """ 
        frogPosition = 0
        lane = 0
        jumps = 0
        while position != len(obstacles) - 1:
            jumps += 1
            bestLane = 0
            postition = frogPosition
            for laneNumber in range(1, 4):
                if laneNumber == lane:
                    continue
                if obstacles[position] != laneNumber:

# kláraði ekki. kinda braindead        

solution = Solution()
print(solution.minSideJumps([0,1,2,3,0]))