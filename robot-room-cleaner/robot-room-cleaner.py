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
        def move_robot(x, y, din):
            robot.clean()
            
            for i in range(4):
                ndin = (din + i) % 4
                dx, dy = faces[ndin]
                nx, ny = x + dx, y + dy
                if((nx, ny) not in visited\
                   and robot.move()):
                    visited.add((nx, ny))
                    move_robot(nx, ny, ndin)
                
                robot.turnRight()
            
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        visited = set([(0, 0)])
        faces = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        move_robot(0, 0, 0)
        
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        