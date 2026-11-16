class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slot_b, self.slot_m, self.slot_s = big, medium, small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.slot_b == 0:
                return False
            self.slot_b -= 1
        elif carType == 2:
            if self.slot_m == 0:
                return False
            self.slot_m -= 1
        elif carType == 3:
            if self.slot_s == 0:
                return False
            self.slot_s -= 1

        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)