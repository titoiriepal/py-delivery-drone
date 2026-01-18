class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


# write your code here
class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int, int] = [0, 0],
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step


robot = BaseRobot(name="Walle", weight=34, coords=[3, -2])
robot.go_forward()
# robot.coords == [3, -1]
robot.go_right(5)
# robot.coords == [8, -1]
print(robot.coords)
