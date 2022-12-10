from abc import abstractclassmethod, ABC


class Player(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractclassmethod
    def info(self):
        "球员的职位"

    def __str__(self):
        return f'name={self.name}, role={self.role}'


class Forward(Player):
    def info(self):
        return f"是前锋"


class MiddleField(Player):
    def info(self):
        return f"是中场"


class DefenseField(Player):
    def info(self):
        return f"是后卫"

        