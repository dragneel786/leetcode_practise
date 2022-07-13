# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def moveRobot(pos, curDir, visited = set()):
            if(pos in visited):
                return
            
            robot.clean()
            visited.add(pos)
            x, y = pos
            for i in range(4):
                newDir = (curDir + i) % 4
                dx, dy = d[newDir]
                nx, ny = x + dx, y + dy
                if((nx, ny) not in visited and robot.move()):
                    moveRobot((nx, ny), newDir, visited)
                robot.turnRight()
            
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
            
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        moveRobot((0, 0), 0)
        
        
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        