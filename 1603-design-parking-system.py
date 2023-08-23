class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.qty_map = {1 : big, 2 : medium, 3 : small}
        self.parking_map = {1 : 0, 2 : 0, 3 : 0}

    def addCar(self, carType: int) -> bool:
        if self.parking_map[carType] < self.qty_map[carType]:
            self.parking_map[carType] += 1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)