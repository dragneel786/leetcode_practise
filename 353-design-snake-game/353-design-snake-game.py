class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.occ = set([(0, 0)])
        self.h, self.w = height, width
        self.f = deque(food)
        self.sn = deque([(0, 0)])
        self.sc = 0

    def move(self, direction: str) -> int:
        food = self.f
        occ, sna = self.occ, self.sn
        prev = self.sc
        at = self.changeDirection(direction, sna[-1])
        if(not at or at in self.occ or self.sc == -1):
            self.sc = -1
            
        elif(food and at == tuple(food[0])):
            self.sc += 1
            occ.add(at)
            food.popleft()
            sna.append(at)
            if(self.sc < len(sna)):
                occ.remove(sna.popleft())
        else:
            occ.remove(sna.popleft())
            sna.append(at)
            occ.add(at)
        
        return self.sc
        
        
    def changeDirection(self, d, at):
        he, wi = self.h, self.w
        change = None
        if(d == "U"):
            if(at[0] == 0):
                return None
            change = [-1, 0]
        elif(d == "D"):
            if(at[0] == he - 1):
                return None
            change = [1, 0]
        elif(d == "R"):
            if(at[1] == wi - 1):
                return None
            change = [0, 1]
        else:
            if(at[1] == 0):
                return None
            change = [0, -1]
        return (at[0] + change[0], at[1] + change[1])
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)