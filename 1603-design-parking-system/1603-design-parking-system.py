class ParkingSystem:
    
    def __init__(self, big: int, medium: int, small: int):
        self.parkings = [[0, big], [0, medium], [0, small]]

    def addCar(self, carType: int) -> bool:
        spot = self.parkings[carType - 1]
        if(spot[0] == spot[1]):
            return False
        spot[0] += 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)