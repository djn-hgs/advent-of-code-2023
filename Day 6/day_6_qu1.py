import math
from dataclasses import dataclass
import math as m


@dataclass
class Race:
    time: int
    distance: int

    def count(self):
        D = self.time ** 2 - 4 * self.distance

        min_p = (self.time - m.sqrt(D)) / 2
        max_p = (self.time + m.sqrt(D)) / 2

        min_int = math.ceil(min_p)

        max_int = math.floor(max_p)

        if is_square(D):
            max_int = max_int - 1
            min_int = min_int + 1

        return 1 + max_int - min_int


def is_square(n):
    x = n // 2
    seen = {x}
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


races = [
    Race(time=54817088, distance=446129210351007)
]

print([r.count() for r in races])
